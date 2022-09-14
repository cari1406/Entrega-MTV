from django.urls import path
from segundaparte.views import familia


urlpatterns = [
    path('familia/', familia),
] 