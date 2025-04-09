from django.urls import path
from user.views import connecting, home

app_name = 'user'

urlpatterns = [
    path('connecting/', connecting, name='connecting'),
    path('', home, name='home'),
]
