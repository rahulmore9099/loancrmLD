from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ai/', include('ai_assistant.urls')),
    path('', include('website.urls')),   # website app

    path('customers/', include('customers.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
   


    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    
]