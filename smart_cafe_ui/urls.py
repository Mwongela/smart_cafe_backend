from django.urls import path

from smart_cafe_ui.views import IndexView, MenusView, OrdersView, FoodsView, MenuAddView, MenuChangeView, \
    OrderChangeView, FoodAddView, FoodChangeView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', MenusView.as_view(), name='menus'),
    path('menu/add/', MenuAddView.as_view(), name="add_menu"),
    path('menu/change/<int:id>/', MenuChangeView.as_view(), name='change_menu'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('orders/change/<int:id>/', OrderChangeView.as_view(), name="change_order"),
    path('food/', FoodsView.as_view(), name='foods'),
    path('food/add/', FoodAddView.as_view(), name='add_food'),
    path('food/change/<int:pk>/', FoodChangeView.as_view(), name='change_food')
]