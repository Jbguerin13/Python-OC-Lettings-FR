from .settings import *

# Use in-memory database for testing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Disable debug mode for tests
DEBUG = False

# Set a default SECRET_KEY for CI/CD tests
SECRET_KEY = 'test-secret-key-for-ci-cd-pipeline-12345'

# Use a fast password hasher for tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
] 