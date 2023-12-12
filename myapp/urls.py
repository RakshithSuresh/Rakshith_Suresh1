from django.urls import path
from .views import contact_list, contact_detail, contact_new, contact_edit, contact_delete

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('contact/<int:pk>/', contact_detail, name='contact_detail'),
    path('contact/new/', contact_new, name='contact_new'),
    path('contact/<int:pk>/edit/', contact_edit, name='contact_edit'),
    path('contact/<int:pk>/delete/', contact_delete, name='contact_delete'),
]