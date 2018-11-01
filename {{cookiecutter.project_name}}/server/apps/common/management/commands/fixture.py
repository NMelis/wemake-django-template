from django.core.management.base import BaseCommand

from server.apps.user.models import User
from server.settings.components import config


class Command(BaseCommand):
    """Создание базовых записей в базу для стартовой работы системы."""

    help = 'Create base fixture'

    def handle(self, *args, **options):
        """End point."""
        login = config('DJANGO_DEFAULT_ADMIN_LOGIN', None)
        password = config('DJANGO_DEFAULT_ADMIN_PASSWORD', None)
        if password is not None or login is not None:
            self.create_super_user(login, password)

    def create_super_user(self, login, password):
        """Создание пользователя."""
        if User.objects.filter(login=login).first():
            return
        User.objects.create_superuser(
            login=login, password=password, status=True,
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully created superuser "{0}"'.format(User.login),
            ),
        )
        self.stdout.write(
            self.style.SUCCESS(
                'Login: {login}\nPassword: {password}'.format(
                    login=login, password=password,
                ),
            ),
        )
