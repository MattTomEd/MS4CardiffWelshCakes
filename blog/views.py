from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Return all posts that have Published status. Order chronologically.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'