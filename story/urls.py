from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views
from .views import (
    IndexView, SingleView, AboutView, StyleView, PageView,
    contact, CategoryDetailView, IndexDetailView, AdDetailView, ReDetailView, FeDetailView, successView
)

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    
    path('page/', views.PageView.as_view(), name='page'),

    path('page/<pk>/', views.IndexDetailView.as_view(), name='post-detail'),
    path('pag/<pk>/', views.AdDetailView.as_view(), name='post-advertise'),
    path('pa/<pk>/', views.ReDetailView.as_view(), name='post-recipe'),
    path('p/<pk>/', views.FeDetailView.as_view(), name='post-featured'),

    path('cat/<pk>/', views.CategoryDetailView.as_view(), name='post-category'),
    
    path('single/', views.SingleView.as_view(), name='single'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('style/', views.StyleView.as_view(), name='style'),
    
    path('contact/', contact, name='email'),
    path('success/', successView, name='success'),
    
]