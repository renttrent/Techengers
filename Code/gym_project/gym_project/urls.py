from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('login.urls')),
    path('dashboard/', include('dashboards.urls')),
    path('admin/', admin.site.urls),
    path('staff/', include('staff.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
