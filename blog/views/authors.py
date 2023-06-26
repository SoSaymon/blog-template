from django.views import generic

from blog.models import User


class AuthorListView(generic.ListView):
    template_name = 'blog/author_list.html'

    model = User
    paginate_by = 10
    context_object_name = 'authors'
    queryset = User.objects.filter(role='author').order_by('-created_at')


class AuthorDetailView(generic.DetailView):
    template_name = 'blog/author_detail.html'

    model = User
    context_object_name = 'author'
