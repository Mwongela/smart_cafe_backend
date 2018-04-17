from django.urls import path

from smart_cafe_ui.views import IndexView

urlpatterns = [
    path('', IndexView.as_view())
]
