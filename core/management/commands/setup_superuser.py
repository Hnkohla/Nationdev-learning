from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates a superuser with specific credentials'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete existing superuser if exists
        User.objects.filter(username='hnkohla').delete()
        
        if not User.objects.filter(username='hnkohla').exists():
            User.objects.create_superuser(
                username='hnkohla',
                email='hnkohla@example.com',
                password='hnkohla123'
            )
            self.stdout.write(self.style.SUCCESS('Superuser hnkohla created successfully'))