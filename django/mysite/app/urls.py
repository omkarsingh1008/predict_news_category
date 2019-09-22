from django.urls import path,include

from . import views
from django.contrib import admin

urlpatterns = [
                path('app/',views.index,name='home'),
                path('app/predict/',views.predict)]
