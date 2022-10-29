from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchedlist, name='html'),
    path('xml/', show_mywatchlist_xml, name='xml'),
    path('json/', show_mywatchlist_json, name='json'),

]