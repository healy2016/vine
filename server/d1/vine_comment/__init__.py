VERSION = (1, 0, 1, 'exp', 0)

def get_version(*args, **kwargs):
    # Don't litter django/__init__.py with all the get_version stuff.
    # Only import if it's actually called.
    from django.utils.version import get_version
    return get_version(*args, **kwargs)