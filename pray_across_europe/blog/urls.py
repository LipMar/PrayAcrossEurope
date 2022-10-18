from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', ArticleListView.as_view(), name = 'blog-home'), #czy to jest ok, że na pierwszej pozycji jest 'blog'??
    path('article-detail/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail' ),
    path('article/new/', ArticleCreateView.as_view(), name = 'article-create'),
    path('article/update/<int:pk>', ArticleUpdateView.as_view(), name = 'article-update'),
    path('article/delete/<int:pk>', ArticleDeleteView.as_view(), name = 'article-delete')
    ]