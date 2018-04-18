from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.generic import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/index.html'


class FoodsView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/foods.html'


class MenusView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/menus.html'


class OrdersView(LoginRequiredMixin, TemplateView):
    template_name = 'ui/orders.html'
