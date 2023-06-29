from django.shortcuts import redirect
from django.views import generic

from blog.models import Post, Comment
from blog.forms import CommentForm


class PostListView(generic.ListView):
    model = Post
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-created_at')


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object, approved=True)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post-detail', pk=post.pk)  # Redirect to the post detail page

        # If the form is invalid, render the detail view with the form and existing comments
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)
