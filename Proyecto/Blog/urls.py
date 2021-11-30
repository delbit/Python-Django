from . import views
from django.urls import path
from Blog.views import blog


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/', blog, name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]