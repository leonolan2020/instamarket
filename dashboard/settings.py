from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'media'),
            os.path.join(BASE_DIR, 'static'),
        ]


SITE_URL='/'
MEDIA_URL = SITE_URL+'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ADMIN_URL = '/admin/'
STATIC_URL = SITE_URL+'static/'
STATIC_ROOT = '/static/'
