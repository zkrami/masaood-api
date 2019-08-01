
from rest_framework.exceptions import APIException


class UnValidLogin(APIException):
    status_code = 442

    default_code = 'UNVALID_LOGIN'
    default_detail = {
        "status": status_code,
        "code": default_code,
        "message": 'Unvalid Login email or password is incorrect '
    }

