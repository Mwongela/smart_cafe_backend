from django.urls import path

from smart_cafe_ui.views import IndexView, MenusView, OrdersView, FoodsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', MenusView.as_view(), name='menus'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('food/', FoodsView.as_view(), name='foods'),
]