# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

from .local import *


DEBUG = False
TEMPLATE_DEBUG = False

STATIC_ROOT = '/www/public/ventanita/static/'

ALLOWED_HOSTS = [
    '.ventanita.soy',
    '.ventanita.soy.',
]
