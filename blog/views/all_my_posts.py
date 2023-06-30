from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from blog.models import Post


class AllMyPostsView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    permission_required = 'blog.can_publish'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)