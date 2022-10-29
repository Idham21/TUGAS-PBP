from django.urls import path
from katalog.views import *

app_name = 'katalog'

urlpatterns = [
    path('', get_all_item, name='show_item'),
]