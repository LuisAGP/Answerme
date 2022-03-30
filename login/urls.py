from django.urls import path
from login.views import *

urlpatterns = [
    path('login/', login_site, name='login'),
    path('logout/', logout_site, name='logout'),
]