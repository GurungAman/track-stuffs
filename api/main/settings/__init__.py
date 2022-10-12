from decouple import config

env = config('ENVIRONMENT', default='DEV')

if env == 'PROD':
    print('Using Production environment')
    from .production import *
else:
    print('Using development settings')
    from .development import *
