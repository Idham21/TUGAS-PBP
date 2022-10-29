from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from mywatchlist.models import MyWatchList

# Create your views here.
def show_mywatchedlist(request):
    mywatchlist = MyWatchList.objects.all()
    context = {
    'watch_list': mywatchlist,
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_xml (request) :
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_json (request) :
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")