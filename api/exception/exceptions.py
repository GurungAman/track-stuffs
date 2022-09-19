from rest_framework.exceptions import APIException
from rest_framework import status


class DuplicateNameError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Object with given data already exists.'
    default_code = 'duplicate'


class InvalidCategoryError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Category does not exist.'
    default_code = 'category'
