from django.contrib import admin

# Register your models here.
from api.models import FoodCategory, Food, MenuCategory, MenuItem, Menu, Order, OrderItem


class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'price', 'image', 'category')


class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'category')


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('menu', 'food')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'food')


admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
