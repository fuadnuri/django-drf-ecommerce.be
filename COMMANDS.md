# packages
django

python-dotenv
djangorestframework
pytest
pytest-django
django-mptt
drf-spectacular
coverage
pytest-cov
pytest-factoryboy

# commands
py -m pip install --ugrade pip

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

coverage run -m pytest
pytest --cov
