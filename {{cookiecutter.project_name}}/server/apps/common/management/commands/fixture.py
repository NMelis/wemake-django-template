from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from server.settings.components import config


class Command(BaseCommand):
    """Создание базовых записей в базу для стартовой работы системы."""

    help = 'Create base fixture'

    def handle(self, *args, **options):
        """End point."""
        username = config('DJANGO_DEFAULT_ADMIN_LOGIN', 'Admin')
        email = config('DJANGO_DEFAULT_ADMIN_EMAIL', 'Admin@example.com')
        password = config('DJANGO_DEFAULT_ADMIN_PASSWORD', 'nimda2018')
        if password and username and email:
            self.create_super_user(username, password, email)

    def create_super_user(self, username, password, email):
        """Создание пользователя."""
        if User.objects.filter(username=username).first():
            self.stdout.write(
                self.style.NOTICE(
                    'Already exists user with is "{0}" login'.format(username),
                ),
            )
            return
        User.objects.create_superuser(
            email=email, username=username, password=password,
        )

        self.stdout.write(
            self.style.SUCCESS(
                'Successfully created superuser "{0}"'.format(User.username),
            ),
        )
        self.stdout.write(
            self.style.SUCCESS(
                'Email: {email}\nLogin: {login}\nPassword: {password}'.format(
                    email=username, username=username, password=password,
                ),
            ),
        )
