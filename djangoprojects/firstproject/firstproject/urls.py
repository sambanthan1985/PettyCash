from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('PettyCash',views.wish)
]
