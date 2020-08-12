from pathlib import Path
import os
import sys
ON_SERVER=True
if '--no-color' in sys.argv:
    ON_SERVER=False

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
if ON_SERVER:

    SITE_URL='/'
    ADMIN_URL = SITE_URL+'admin/'

    MEDIA_URL = SITE_URL+'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    STATIC_URL = SITE_URL+'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
else:
    SITE_URL='/'
    ADMIN_URL = SITE_URL+'admin/'

    MEDIA_URL = SITE_URL+'media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    STATIC_URL = SITE_URL+'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


