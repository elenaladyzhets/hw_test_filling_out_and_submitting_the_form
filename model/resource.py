import os

def path(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test', 'resources', file_name))