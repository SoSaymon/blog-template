from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user,
        }
        return render(request, 'blog/profile.html', context=context)
    