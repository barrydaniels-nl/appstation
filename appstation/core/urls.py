from django.contrib import admin
from django.urls import path, include
from core.views import SetupView

urlpatterns = [
    path('setup/', SetupView.as_view(), name='setup'),
    path('setup/<id:int>/', include('appstation.core.urls')),
]
