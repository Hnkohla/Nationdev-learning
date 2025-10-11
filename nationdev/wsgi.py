"""
WSGI config for NationDev
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nationdev.settings')
application = get_wsgi_application()