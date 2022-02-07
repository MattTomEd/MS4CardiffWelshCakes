from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .forms import CommentForm
from .models import Post


class post_list(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

class post_content(generic.DetailView):
    model = Post
    template_name = 'post_content.html'
    

def post_detail(request, slug):
    template_name = 'post_content.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})