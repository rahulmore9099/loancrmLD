from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ai/', include('ai_assistant.urls')),
    path('', include('website.urls')),   # website app

    path('customers/', include('customers.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]