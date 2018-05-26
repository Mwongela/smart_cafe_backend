from django import forms

from api.models import Food


class AddFoodForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['name', 'calories', 'price', 'image', 'category', 'archived']