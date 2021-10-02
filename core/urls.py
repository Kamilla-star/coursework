from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('contact', views.contact, name='contact'),
    path('dashboard/edit-task/<str:id>/', views.edit_task, name='edit_task'),
    path('dashboard/delete-task/<str:id>/', views.delete_task, name='delete_task'),
]