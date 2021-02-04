from django.conf import settings
from django.contrib import admin
from django.contrib import auth
from django.urls import path, include
from django.conf.urls import url

import APP_NAME

urlpatterns = [
    url(r'^', include(('APP_NAME.urls', 'APP_NAME'), namespace="APP_NAME")),
]