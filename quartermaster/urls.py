from django.urls import path
from django.conf.urls import *
from . import views

app_name = 'QuarterMaster'

urlpatterns = [
    path('pantry/', views.PantryListView.as_view(), name='mypantry'),
    path('pantry/<int:pk>', views.PantryItemDetail.as_view(), name='pantryitem'),
    path('pantry/add_item/', views.AddItemView.as_view(), name='add_item'),
] 