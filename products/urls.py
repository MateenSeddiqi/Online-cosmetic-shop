from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback/', views.displayFeedback, name='displayFeedback'),
    path('add-feedback/', views.add_feedback, name='add-feedback'),
    path('update-feedback/<int:pk>/', views.update_feedback, name='update-feedback'),
    path('delete-feedback/<int:pk>/', views.delete_feedback, name='delete-feedback'),
    path('displayProduct/', views.displayProduct, name='displayProduct'),
    path('addProduct/', views.addProduct, name='addProduct'),
]
