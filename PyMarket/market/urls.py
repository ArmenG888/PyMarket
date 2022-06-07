from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("item/<pk>/", views.items_selling, name="items_selling"),
    path("item/<pk>/<id>/", views.item_selling, name="item_selling_detail"),
]
