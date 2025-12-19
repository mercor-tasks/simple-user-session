import functools

from django.http import JsonResponse

from .exceptions import CustomHttpError


def handle_exception(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomHttpError as ce:
            return JsonResponse(
                {
                    "message": ce.message,
                },
                status=ce.status_code)
    return wrapper
