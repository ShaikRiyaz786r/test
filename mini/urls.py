from django.contrib import admin
from django.urls import path,include
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/', details),
    path('dem/',dem)
]
