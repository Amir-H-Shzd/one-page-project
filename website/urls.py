from django.urls import path
from website.views import *

urlpatterns = [
    path('', Home_view, name='home'),
]
