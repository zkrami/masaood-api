
from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 440

    default_code = 'SERVICE_UNAVAILABLE'
    default_detail = {
        "status": status_code,
        "code": default_code,
        "message": 'Service temporarily unavailable, try again later.'
    }



class MobileVerificationError(APIException):
    status_code = 441

    default_code = 'MOBILE_VERIFICATION_ERROR'
    default_detail = {
        "status": status_code,
        "code": default_code,
        "message": 'Failed to verify your phone number'
    }
