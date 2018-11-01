# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler

from server.apps.common.common import ErrorFormatter


class UserNotFoundError(APIException):
    """User not found error."""

    status_code = 404
    default_detail = 'User not found.'


class BugsTakenOutFieldInvalid(APIException):
    """Need field not found."""

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Need field not found in the bugs_taken_out.'


class InstanceAlreadyHaveActivateStatus(APIException):
    """Instance already have status error."""

    status_code = status.HTTP_409_CONFLICT
    default_detail = 'This instance already have status "activate"'


class RoutingSheetAreNotForTheCurrentUser(APIException):
    """Routing sheet are not for the current user."""

    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Routing sheet are not for you'


class BadCredentialsError(APIException):
    """Bad credentials error."""

    status_code = 404
    default_detail = 'Bad Credentials.'


def custom_exception_handler(exc=None, context=None):
    """Изменение вида ошибок.

    Args:
        Эти параметры передает raise ValidationError()
        exc         (ValidationError): Класс исключение
        context     (dict): Контекст

        А эти параметры нужно передовать в ручную при использование вебсокета:
        server.apps.websocket_channels.custom_websocker_consumers

        errors      (List or None): Список ошибок
        status_code (int):          Статус кода

    Returns:
        dict: Мапка с параметрами для вызова Exception

    """
    response = exception_handler(exc, context)
    if response is not None:
        errors = []
        if 'non_field_errors' in response.data:
            for error in response.data['non_field_errors']:
                errors.append(error)
        else:
            errors = response.data
        response.data = ErrorFormatter.format(errors, response.status_code)

    return response
