from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='authentication')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

