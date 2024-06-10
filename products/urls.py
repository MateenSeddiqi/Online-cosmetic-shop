from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('feedback/', views.displayFeedback, name='displayFeedback'),
    path('add-feedback/', views.add_feedback, name='add-feedback'),
    path('update-feedback/<int:pk>/', views.update_feedback, name='update-feedback'),
    path('delete-feedback/<int:pk>/', views.delete_feedback, name='delete-feedback'),
    path('manageProduct/', views.manageProduct, name='manageProduct'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
