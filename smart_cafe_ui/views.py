from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response, redirect, get_object_or_404

# Create your views here.
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, UpdateView, CreateView, DeleteView

from api.models import Food
from smart_cafe_ui.forms import AddFoodForm


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/index.html'


class FoodsView(LoginRequiredMixin, ListView):
    template_name = 'ui/foods.html'
    model = Food
    context_object_name = 'food_list'
    paginate_by = 14
    queryset = Food.objects.all().order_by('-id')


class FoodAddView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['name', 'calories', 'price', 'image', 'category']
    template_name = 'ui/add_food.html'
    success_url = reverse_lazy('ui:foods')


class FoodChangeView(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ['name', 'calories', 'price', 'image', 'category', 'archived']
    template_name = 'ui/change_food.html'
    success_url = reverse_lazy('ui:foods')


class MenusView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/menus.html'


class MenuAddView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/add_menu.html'


class MenuChangeView(LoginRequiredMixin, TemplateView):
    pass


class OrdersView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/orders.html'


class OrderChangeView(LoginRequiredMixin, TemplateView):
    pass
