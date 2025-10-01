from django.contrib import admin
from django.urls import path
from main.views import recommend_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recommend_view, name='recommend'),
]
