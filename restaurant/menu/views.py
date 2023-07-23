from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import IngredientForm, MenuItemForm, RecipeRequirementForm
# Create your views here.

class homeView(LoginRequiredMixin, TemplateView):
    template_name = 'menu/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_item"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context


class IngredientView(LoginRequiredMixin, ListView):
    template_name = 'menu/ingredients_list.html'
    model = Ingredient

class newIngredientView(LoginRequiredMixin, CreateView):
    template_name = 'menu/add_ingredient.html'
    model = Ingredient
    form_class = IngredientForm

class MenuView(LoginRequiredMixin, ListView):
    template_name = 'menu/menu_list.html'
    model = MenuItem

class newMenuView(LoginRequiredMixin, CreateView):
    template_name = 'menu/add_menu_list.html'
    model = MenuItem
    form_class = MenuItemForm

class newRecipeRequirement(LoginRequiredMixin, CreateView):
    template_name = 'menu/add_recipe_requirement'
    model = RecipeRequirement
    form_class = RecipeRequirementForm

class purchaseView(LoginRequiredMixin, ListView):
    template_name = 'menu/purchase_list'
    model = Purchase

class newPurchaseView(LoginRequiredMixin, CreateView):
    template_name = 'menu/add_purchase_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = [X for X in MenuItem.objects.all() if X.available]
        return context
    
    def post(self, request):
        menu_item_id = request.POST['menu_item']
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.reciperequirement_set
        purchase = Purchase(menu_item=menu_item)

        purchase.save()
    
        return redirect("/purchase")
    

class billView(LoginRequiredMixin, TemplateView):
    template_name = 'menu/bill.html'

def log_out(request):
    logout(request)
    return redirect("/")