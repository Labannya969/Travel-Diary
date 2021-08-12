from django.urls import path
from django.conf.urls import url
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views #. means current directory

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    #path('user/<str:username>/', UserPostListView.as_view(), name='user-post'),
    #path('user/<str:username>/', UserPostListView.as_view(),name='user-post'),
    url(r'^user/(?P<username>\w{0,50})/$', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
# <app>/<model>_<viewtype>.html

