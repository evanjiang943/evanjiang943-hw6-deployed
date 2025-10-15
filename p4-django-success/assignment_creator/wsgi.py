"""
WSGI config for assignment_creator project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment_creator.settings')

application = get_wsgi_application()

