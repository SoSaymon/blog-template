from django.shortcuts import render, redirect
from django.views import View

from blog.forms.edit_profile import EditProfileForm


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user,
        }
        return render(request, 'blog/profile.html', context=context)


class EditProfileView(View):
    form_class = EditProfileForm
    template_name = 'blog/edit_profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, context={'form': form})
