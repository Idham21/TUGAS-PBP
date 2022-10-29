from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def get_all_item(request) :
    item = CatalogItem.objects.all()
    context = {
        "item" : item
    }
    return render(request, "katalog.html", context)