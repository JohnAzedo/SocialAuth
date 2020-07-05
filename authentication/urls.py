# from authentication.views import Login
from django.urls import path
from django.views.generic import RedirectView


app_name = 'authentication'

urlpatterns = [
    path('', RedirectView.as_view(permanent=False, url='/accounts/login/'))
]
