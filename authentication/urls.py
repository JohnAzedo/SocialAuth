from authentication.views import Login
from django.urls import path

app_name = 'authentication'

urlpatterns = [
    path('', Login.as_view(), name="login")
]
