from django.shortcuts import redirect, render
from .models import item, items
from .forms import item_sell
from django.contrib.auth.decorators import login_required
import random

def home(request):
    return render(request, "market/home.html", {'items': items.objects.all()})

def items_selling(request,pk):
    itemss = items.objects.all().filter(id=pk)[0].items.filter(selling=True)
    return render(request, "market/item-selling.html", {'items':itemss})

def item_selling(request,pk):
    item_x = item.objects.all().filter(id=pk)[0]
    return render(request, "market/item-selling-detail.html", {"item":item_x})

def item_buy(request,pk):
    item_x = item.objects.all().filter(id=pk)[0]
    if request.user.profile.coins >= item_x.price and item_x.owner != request.user:
        item_x.owner.profile.coins += round(item_x.price,2)
        item_x.owner.profile.save()
        request.user.profile.coins -= round(item_x.price,2)
        request.user.profile.save()
        item_x.owner = request.user 
        item_x.selling = False
        item_x.save()
    if item_x.owner == request.user:
        item_x.selling = False
        item_x.save()
    
    return redirect('items_selling', pk=item_x.belongs_to.id)

def inventory(request):
    items_owned = item.objects.all().filter(owner=request.user, selling=False)
    return render(request, "market/inventory.html", {'items':items_owned})

def item_sell_view(request, pk):
    item_x = item.objects.all().filter(id=pk)[0]
    if request.method == 'POST':
        form = item_sell(request.POST)
        if form.is_valid():
            price = form.cleaned_data['price']
            print(price)
            item_x.price = price
            item_x.selling = True
            item_x.save()
            redirect("item_selling_detail", item_x.id)          
    else:
        form = item_sell()
    
    return render(request, "market/sell.html", {'form':form, 'item':item_x})


def create_item(request, x, how_many):
    item_x = items.objects.get(name=x)
    for i in range(how_many):
        new_item = item.objects.create(owner=request.user, belongs_to=item_x, selling=True, price=(random.randint(9,124)/100))
        item_x.items.add(new_item)
    return redirect('home')

def open_case(request):
    x = random.randint(1,1000)
    request.user.profile.coins -= 5
    request.user.profile.save()
    if x > 950 and x < 1000:
        item_x = items.objects.all().filter(rarity="Legendary")
        y = random.randint(0, len(item_x)-1)
        new_item = item.objects.create(owner=request.user, belongs_to=item_x[y], selling=False, price=0)
        item_x[y].items.add(new_item)
    elif x > 800 and x <= 950:
        item_x = items.objects.all().filter(rarity="Rare")
        y = random.randint(0, len(item_x)-1)
        new_item = item.objects.create(owner=request.user, belongs_to=item_x[y], selling=False, price=0)
        item_x[y].items.add(new_item)
    else:
        item_x = items.objects.all().filter(rarity="Common")
        y = random.randint(0, len(item_x)-1)
        new_item = item.objects.create(owner=request.user, belongs_to=item_x[y], selling=False, price=0)
        item_x[y].items.add(new_item)  
    return redirect('inventory')