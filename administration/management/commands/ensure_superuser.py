from decouple import config
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Ensures a superuser exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        username = config('DJANGO_SUPERUSER_USERNAME', default=None)
        email = config('DJANGO_SUPERUSER_EMAIL', default='')
        password = config('DJANGO_SUPERUSER_PASSWORD', default=None)
        
        if not username or not password:
            self.stdout.write(self.style.ERROR(' DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD must be set'))
            return
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f' Superuser created: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f' Superuser {username} already exists'))