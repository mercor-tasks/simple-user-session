class CustomHttpError(Exception):
    status_code: int = 200
    message: str = ""

    def __init__(self, message):
        self.message = message


class BadRequestError(CustomHttpError):
    status_code = 400
    message = "Bad Request"


class NotFoundError(CustomHttpError):
    status_code = 404
    message = "Not Found"
