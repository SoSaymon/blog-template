from django import forms
from blog.models import User
from django.utils.translation import gettext_lazy as _


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'bio',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your bio here...',
                                         'style': 'resize:none;'}),
        }
        labels = {
            'username': '',
            'email': '',
            'bio': '',
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists() and username != self.instance.username:
            raise forms.ValidationError(_('Username already exists'))
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists() and email != self.instance.email:
            raise forms.ValidationError(_('Email already exists'))
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.bio = self.cleaned_data['bio']
        if commit:
            user.save()
        return user
