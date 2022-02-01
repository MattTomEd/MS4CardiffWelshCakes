from django.views import generic
from .models import Post
from django.utils import timezone

class post_list(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

class post_detail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'