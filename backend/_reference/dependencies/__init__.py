from app.schemas.common_schema import ApiResponseDTO
from app.enums.user_enum import UserProvider
from app.schemas.auth_schema import JwtTokenDTO, LoginRequestDTO, SocialLoginRequestDTO
from app.services.auth_service import AuthService, get_auth_service