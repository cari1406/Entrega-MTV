from django.urls import path
from carpetadjango.views import *

urlpatterns = [
    path("", inicio),
    path('persona/', persona),
    path('contacto/', contacto),
    path('curso/', curso),
    path('profesor/', profesor),
] 