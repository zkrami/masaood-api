
from rest_framework.exceptions import APIException


class OrderIsNotAssigned(APIException):
    status_code = 452

    default_code = 'ORDER_IS_NOT_ASSIGNED'
    default_detail = {
        "status": status_code,
        "code": default_code,
        "message": 'Order is not assigned to center'
    }


class OrderIsDelivered(APIException):
    status_code = 453

    default_code = 'ORDER_IS_DELIVERED'
    default_detail = {
        "status": status_code,
        "code": default_code,
        "message": 'Order is in delivered state'
    }


class CenterHasNoProduct(APIException):
    status_code = 454
    default_code = 'CENTER_HAS_NO_PRODUCT'
    default_detail = {
        "status": status_code,
        "code": default_code,
        "message": 'Center does not have a product'
    }
