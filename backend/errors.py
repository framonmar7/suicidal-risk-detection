from rest_framework.exceptions import APIException
from rest_framework import status

class EmptyText(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail="Empty comment."):
        super().__init__({"error": detail})

class TextTooShort(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, min_len: int, got_len: int):
        msg = f"Minimum length {min_len} characters; got {got_len}"
        super().__init__({"error": msg})

class TextTooLong(APIException):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, max_len: int, got_len: int):
        msg = f"Maximum length {max_len} characters; got {got_len}"
        super().__init__({"error": msg})
