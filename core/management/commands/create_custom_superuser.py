from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Creates a superuser with specific credentials'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='hnkohla').exists():
            User.objects.create_superuser(
                username='hnkohla',
                email='hnkohla@example.com',
                password='hnkohla123'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))