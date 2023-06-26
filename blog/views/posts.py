
from django.views import generic

from blog.models import Post

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created_at')


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
