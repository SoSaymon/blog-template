from django.contrib import admin

from .models import Post, Category, Tag, Comment, User

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(User)

# admin site customization
admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog Admin'
admin.site.index_title = 'Blog Admin'
