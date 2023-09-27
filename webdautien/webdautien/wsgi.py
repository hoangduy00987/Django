"""
WSGI config for webdautien project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

import django.core.wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdautien.settings')

application = django.core.wsgi.get_wsgi_application()
