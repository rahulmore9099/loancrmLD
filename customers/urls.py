# from django.urls import path
# from . import views

# urlpatterns = [

#     path('', views.customer_list, name='customer_list'),
#     path('add/', views.add_customer, name='add_customer'),

#     path('add-pl/<int:pk>/', views.add_pl, name='add_pl'),
#     path('add-bl/<int:pk>/', views.add_bl, name='add_bl'),

#     # NEW
#     path('view/<int:pk>/', views.customer_detail, name='customer_detail'),
#     path('edit/<int:pk>/', views.edit_customer, name='edit_customer'),
#     path('delete/<int:pk>/', views.delete_customer, name='delete_customer'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    #path('', views.dashboard, name='dashboard'),
    path("dashboard/", views.dashboard, name="dashboard"),
    
    path('', views.customer_list, name='customer_list'),
    path('add/', views.add_customer, name='add_customer'),

    path('view/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('edit/<int:pk>/', views.edit_customer, name='edit_customer'),
    path('delete/<int:pk>/', views.delete_customer, name='delete_customer'),

    path('add-pl/<int:pk>/', views.add_pl, name='add_pl'),
    path('add-bl/<int:pk>/', views.add_bl, name='add_bl'),
    path('status/add/<int:pk>/', views.add_status, name='add_status'),
path('status/history/<int:pk>/', views.status_history, name='status_history'),


]