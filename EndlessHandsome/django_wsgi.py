#!/usr/bin/env python
# coding: utf-8

import os
import sys
import site


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

VENV_DIR = os.path.join(os.path.dirname(BASE_DIR), 'venv')

site.addsitedir(os.path.join(VENV_DIR, 'lib/python3.4/site-packages'))

# Activate your virtual env
activate_env = os.path.join(VENV_DIR, 'bin/activate_this.py')

exec(compile(open(activate_env).read(), activate_env, 'exec'), dict(__file__=activate_env))


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EndlessHandsome.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()