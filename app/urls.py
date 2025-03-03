from django.contrib import admin
from django.urls import path, include  # O 'include' é necessário

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('affi.urls')),
]
