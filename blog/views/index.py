from django.shortcuts import render

from blog.models import Post


def index(request):
    posts = Post.objects.order_by('-created_at')[:4]
    context = {'posts': posts}
    return render(request, 'index.html', context=context)