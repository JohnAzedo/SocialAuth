from core.views import Login
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', Login.as_view(), name="login")
]
