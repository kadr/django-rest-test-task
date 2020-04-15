from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Direction.urls')),
    path('api/', include('Course.urls')),
    path('api/', include('Lesson.urls')),
]
