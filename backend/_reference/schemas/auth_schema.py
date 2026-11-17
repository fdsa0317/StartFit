from pydantic import BaseModel
from app.enums.user_enum import UserProvider

# DTO
class LoginRequestDTO(BaseModel):
    user_email: str
    user_password: str | None = None
    user_provider: UserProvider | None = None

    class Config:
        from_attributes = True

        
class SocialLoginRequestDTO(BaseModel):
    user_email: str
    user_provider_id: str | None = None
    user_provider:  UserProvider | None = None

    class Config:
        from_attributes = True


class JwtTokenDTO(BaseModel):
    access_token: str | None = None
    refresh_token: str | None = None

    class Config:
        from_attributes = True
