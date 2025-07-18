from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.user.urls')),
    path('cars/', include('apps.car.urls')),
    path('payments/', include('apps.payment.urls')),
]
