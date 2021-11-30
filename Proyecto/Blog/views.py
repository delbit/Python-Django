from django.shortcuts import render
from django.views import generic
from .models import Post
from django.template import loader
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'Blog/index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'Blog/post_detail.html'

def blog(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'Blog/index.html', {'post_list': posts})