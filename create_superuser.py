from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

def create_superuser():
    User = get_user_model()
    if not User.objects.filter(username='hnkohla').exists():
        User.objects.create_superuser('hnkohla', 'admin@example.com', 'hnkohla123')
        print('Superuser created successfully')
    else:
        print('Superuser already exists')