from django.urls import path
from mywatchlist.views import *
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('create-task/', create_task, name='create_task'),
    path('register/', register, name='register')



]