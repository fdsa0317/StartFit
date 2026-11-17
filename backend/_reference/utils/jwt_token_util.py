import os
from dotenv import load_dotenv
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

# 1. access_token 생성하는 함수
def generate_access_token(user_claim: UserClaimDTO) -> str:
    # dto -> dict
    claims = user_claim.model_dump()

    # access_token: 1분~5분
    expire = datetime.now(timezone.utc) + timedelta(days=1)
    access_token = jwt.encode(
        {
            **claims,
            "exp": expire
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return access_token

# 2. refresh_tokken 생성하는 함수
def generate_refresh_token(user_claim: UserClaimDTO) -> str:
    # dto -> dict
    claims = user_claim.model_dump()

    # refresh_tokken: 30일
    expire = datetime.now(timezone.utc) + timedelta(days=30)
    refresh_tokken = jwt.encode(
        {
            **claims,
            "exp": expire
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return refresh_tokken


# 3. token_parsing 함수 (token -> user_info)
def parse_token(token: str) -> UserClaimDTO:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    user_id = payload["id"]
    user_email = payload["user_email"]
    user_provider = payload["user_provider"]
    
    # UserClaimDTO.model_validate(payload)

    return UserClaimDTO(
        id=user_id,
        user_email=user_email,
        user_provider=user_provider
    )


# 4. refresh_token을 이용해서 access_token 재발급
def reissue_access_token(refresh_token: str) -> str:
    claims = parse_token(refresh_token)
    new_access_token = generate_access_token(claims)
    return new_access_token