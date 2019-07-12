from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='4irk1^hvbazfx=h@w5sq)hnus6%xx@xc6&i(f6#=#(=pt(^q)c')
DEBUG = env.bool('DJANGO_DEBUG', default=True)
