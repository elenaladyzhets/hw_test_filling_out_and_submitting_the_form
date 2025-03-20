import os
import test


def path(value):
    return os.path.abspath(os.path.join(os.path.dirname(test.__file__), f'resources/{value}'))
