from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("items/<pk>/", views.items_selling, name="items_selling"),
    path("item/<pk>/", views.item_selling, name="item_selling_detail"),
    path("item/<pk>/buy", views.item_buy, name="item_buy"),
    path("item/<pk>/sell/", views.item_sell, name="item_sell"),
    path("inventory/", views.inventory, name="inventory")
]
