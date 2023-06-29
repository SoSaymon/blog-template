from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your comment '
                                                                                                'here...',
                                             'style': 'resize:none;'}),
        }
        labels = {
            'content': '',
        }
