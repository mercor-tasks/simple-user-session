from utils.exceptions import BadRequestError, NotFoundError

from .models import SiteUser


def get_user_in_session(request) -> SiteUser:
    user_id = request.session.get('user_id')
    if user_id is None:
        return None

    user = SiteUser.objects.filter(user_id=user_id)
    if not user.exists():
        raise NotFoundError(f"User with {user_id} not found in DB.")

    return user.first()
