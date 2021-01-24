from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser
from rest_framework import generics, viewsets, permissions


from .forms import AddPantryItem
from .models import PantryItem, Grocerylist


class PantryListView(LoginRequiredMixin, ListView):
    model = PantryItem
    template_name = 'my_pantry1.html'
    
   
   

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PantryItemDetail(DetailView):
    model = PantryItem
    template_name = 'pantry_detail.html'

class AddItemView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = PantryItem
    form_class = AddPantryItem
    template_name = 'add_item.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('quartermaster:mypantry')