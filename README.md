a demonstration of using swagger with django project

Steps
# 1 pip install django-rest-swagger

# 2 Add 'rest_framework_swagger' to INSTALLED_APPS in Django settings.

settings.py

INSTALLED_APPS = [
    ...
    'rest_framework_swagger',
]

# 3 changes in urls.py

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Vigyaa API docs')

# 4 add this in url pattern
urlpatterns = [
    url('apidocumentation', schema_view)
] 


# 5 can be accessed from localhost:8000/apidocumentation

