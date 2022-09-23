from django.contrib import admin
from django.urls import path
from carpetadjango.views import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path("persona/", persona),
]