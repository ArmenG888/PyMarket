from django.shortcuts import redirect, render
from .models import item, items

def home(request):
    return render(request, "market/home.html", {'items': items.objects.all()})

def items_selling(request,pk):
    itemss = items.objects.all().filter(id=pk)[0].items.filter(selling=True)
    print(itemss)
    return render(request, "market/item-selling.html", {'items':itemss})

def item_selling(request,pk):
    item_x = item.objects.all().filter(id=pk)[0]
    return render(request, "market/item-selling-detail.html", {"item":item_x})

def item_buy(request,pk):
    item_x = item.objects.all().filter(id=pk)[0]
    if request.user.profile.coins >= item_x.price and item_x.owner != request.user:
        item_x.owner.profile.coins += item_x.price
        item_x.owner.profile.save()
        request.user.profile.coins -= item_x.price
        request.user.profile.save()
        item_x.owner = request.user 
        item_x.selling = False
        item_x.save()

    return redirect('item_selling_detail', pk=pk)

def inventory(request):
    items_owned = item.objects.all().filter(owner=request.user)
    return render(request, "market/inventory.html", {'items':items_owned})

def item_sell(request, pk):
    pass