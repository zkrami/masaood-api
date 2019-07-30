
from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 503

    default_code = 'service_unavailable'
    default_detail = {
        "status": status_code,
        "code": default_code,
        "message": 'Service temporarily unavailable, try again later.'
    }
