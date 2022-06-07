from django.shortcuts import render
from .models import item, items

def home(request):
    return render(request, "market/home.html", {'items': items.objects.all()})

def items_selling(request,pk):
    itemss = items.objects.all().filter(id=pk)[0].items.filter(selling=True)
    print(itemss)
    return render(request, "market/item-selling.html", {'items':itemss})

def item_selling(request,pk,id):
    item_x = item.objects.all().filter(id=id)[0]
    return render(request, "market/item-selling-detail.html", {"item":item_x})