# -*- coding: utf-8 -*-


class ErrorFormatter:
    """Класс используется для форматирования ошибок."""

    @staticmethod
    def format(errors, status_code):
        """Форматирует ошибки в стандартный вид."""
        return {
            'errors': errors,
            'status_code': status_code,
            'is_error': True,
        }


def get_exception_data(exception):
    """Получение результата вызова исключении.

    Это используеться только для Документации API (swagger).
    """
    from server.api.exceptions import custom_exception_handler
    return getattr(custom_exception_handler(exception()), 'data')
