"""
WSGI config for emojrnl project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'emojrnl.settings_production':
    os.environ['HTTPS'] = "on"
    from dj_static import Cling
    application = Cling(get_wsgi_application())
else:
    application = get_wsgi_application()
