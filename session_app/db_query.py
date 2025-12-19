from utils.exceptions import BadRequestError, NotFoundError

from .models import SiteUser


def get_user_by_username(username: str) -> SiteUser:
    user = SiteUser.objects.filter(username=username)
    if not user.exists():
        raise NotFoundError(f"User with username {username} not found")

    return user.first()


def validate_user_password(user: SiteUser, password_hashed: str):
    if user.password != password_hashed:
        raise BadRequestError("Invalid password")
