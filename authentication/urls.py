from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView


app_name = 'authentication'

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(permanent=False, url='/accounts/login/'))
]
