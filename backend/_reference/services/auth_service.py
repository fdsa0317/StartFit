import os
from dotenv import load_dotenv
from fastapi import Depends, HTTPException, status
from app.repositories.redis_repository import get_redis_repository, RedisRepository
from app.utils.security_util import verify_password
from app.utils.jwt_token_util import (
    parse_token, generate_access_token, generate_refresh_token, reissue_access_token
)
from app.schemas.auth_schema import JwtTokenDTO, LoginRequestDTO, SocialLoginRequestDTO

load_dotenv()
TOKEN_BLACKLIST_PREFIX = os.getenv("TOKEN_BLACKLIST_PREFIX")
REFRESH_TOKEN_PREFIX = os.getenv("REFRESH_TOKEN_PREFIX")

# 예외처리
# 트랜잭션 관리
class AuthService:

    def __init__(
            self, 
            redis_repo: RedisRepository,
            user_service: UserService
        ):
        self.redis_repo = redis_repo
        self.user_service = user_service


    # redis에 refresh_token 저장
    # key - 콜론 체이닝
    async def save_refresh_token(self, user_id: int, refresh_token: str) -> None:
        try:
            key=f"{REFRESH_TOKEN_PREFIX}{user_id}"
            ex = 60 * 60 * 24 * 30 # 30일
            await self.redis_repo.set(key, refresh_token, ex=ex)
            
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="save_refresh_token 오류"
            )


    # redis에 등록된 refresh_token가 유효한지 검사
    async def validate_refresh_token(self, user_id: int, refresh_token: str) -> bool:
        key=f"{REFRESH_TOKEN_PREFIX}{user_id}"
        saved_token = await self.redis_repo.get(key)
        return refresh_token == saved_token


    # redis에 등록된 refresh_token을 삭제 
    async def delete_refresh_token(self, user_id: int):
        key=f"{REFRESH_TOKEN_PREFIX}{user_id}"
        await self.redis_repo.delete(key)


    # redis에 등록된 access_token 무효화 -> 블랙리스트로 등록(로그아웃)
    async def save_blacklisted_token(self, access_token: str) -> None:
        try:
            key = f"{TOKEN_BLACKLIST_PREFIX}{access_token}"
            ex = 60 * 60 * 24

            await self.redis_repo.set(key, "blacklisted", ex=ex)

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="save_blacklisted_token 오류"
            )


    # redis에 블랙리스트로 등록되어있는지 확인
    async def is_blacklisted_token(self, access_token: str) -> bool:
        key = f"{TOKEN_BLACKLIST_PREFIX}{access_token}"
        # True -> 블랙리스트
        # False -> 사용가능
        return await self.redis_repo.exists(key)

    # 로그인
    async def login(self, login_request_dto: LoginRequestDTO) -> JwtTokenDTO:
        # 1. 회원 조회
        user_in_db = await self.user_service.get_user_by_email_and_provider(
            login_request_dto.user_email, 
            login_request_dto.user_provider
        )

        # 2. 비밀번호 검증(단방향 검사)
        if not verify_password(
            login_request_dto.user_password, # 플레인 비밀번호
            user_in_db.user_password # 암호화된 비밀번호
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="verify_password 비밀번호 불일치"
            )

        # 3. JWT 토큰 만들기
        # - 유저의 정보 중 최소한의 정보만 claim에 담기
        user_id = user_in_db.id
        claims = UserClaimDTO(
            id=user_id,
            user_email=user_in_db.user_email,
            user_provider=user_in_db.user_provider
        )

        # - 유틸 함수를 이용해서 토큰을 만든다(refresh, access)
        access_token = generate_access_token(claims)
        refresh_token = generate_refresh_token(claims)

        # 4. refresh를 redis에 저장
        await self.save_refresh_token(user_id, refresh_token)

        # 5. 토큰 반환
        return JwtTokenDTO(
            access_token=access_token,
            refresh_token=refresh_token
        )

    # 소셜 로그인
    async def social_login_or_none(self, social_user: SocialLoginRequestDTO) -> JwtTokenDTO | None:
        user_in_db = await self.user_service.get_user_by_email_and_provider(
            social_user.user_email,
            social_user.user_provider
        )

        if not user_in_db:
            return None

        user_id = user_in_db.id
        claims = UserClaimDTO(
            id=user_id,
            user_email=user_in_db.user_email,
            user_provider=user_in_db.user_provider
        )

        access_token = generate_access_token(claims)
        refresh_token = generate_refresh_token(claims)
        await self.save_refresh_token(user_id, refresh_token)

        return JwtTokenDTO(
            access_token=access_token,
            refresh_token=refresh_token
        )






    # 로그아웃
    async def logout(self, user_id: int, tokens: JwtTokenDTO) -> None:
        # 1. token -> decode -> 필수정보가져온다.(컨트롤러 Depends)
        # 2. 블랙리스트에 토큰(accessTken) 등록
        access_token = tokens.access_token
        await self.save_blacklisted_token(access_token)
        # 3. user_id가 필요 -> 토큰 삭제 
        await self.delete_refresh_token(user_id)
        
        





# 레포지토리 주입 팩토리 함수
def get_auth_service(
    redis_repo: RedisRepository = Depends(get_redis_repository),
    user_service: UserService = Depends(get_user_service)
):
    return AuthService(redis_repo, user_service)


    # refresh -> access 재발급

