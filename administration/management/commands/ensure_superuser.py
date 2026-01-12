from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username='paahs.edu.bd').exists():
            User.objects.create_superuser('paahs.edu.bd', 'asad@gmail.com', 'school118946')
            self.stdout.write('✅ Superuser created: admin / admin123456')
        else:
            self.stdout.write('Superuser already exists')