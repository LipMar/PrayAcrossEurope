from django.urls import path
from . import views
from .views import ContactView, ContactSuccessView, DownloadView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'core-home'),
    path('about/', views.about, name = 'core-about'),
    path('contact/', ContactView.as_view(), name = 'core-contact'),
    path('success/', ContactSuccessView.as_view(), name = 'success'),
    path('downloads/', DownloadView.as_view(), name = 'core-downloads'),
]
