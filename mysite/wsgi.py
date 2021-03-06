#!d:/Python27/python.exe
"""
WSGI config for mysite project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

sys.path.append('D:/Courses/WebDesign/mysite/mysite/')
sys.path.append('D:/Courses/WebDesign/mysite/')
sys.path.append('D:/Courses/WebDesign/')
sys.path.append('D:/python27/')
sys.path.append('D:/sqlite3/')
sys.path.append('D:/Python27/Lib/site-packages/')
sys.path.append('D:/Python27/Lib/site-packages/django/')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
