from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='Post title')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, help_text='Post author')
    tags = models.ManyToManyField('Tag', blank=True, help_text='Post tags')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, default='Uncategorized',
                                 help_text='Post category')

    class Meta:
        ordering = ['-updated_at']
        permissions = (
            ("can_publish", "Can publish posts"),
            ("can_edit", "Can edit posts"),
            ("can_delete", "Can delete posts"),

        )

    def __str__(self):
        return self.title

    # SETTERS
    def set_title(self, title):
        self.title = title
        self.save()

    def set_content(self, content):
        self.content = content
        self.save()

    def set_author(self, author):
        self.author = author
        self.save()

    def set_category(self, category):
        self.category = category
        self.save()

    def set_tags(self, tags):
        self.tags = tags
        self.save()

    # GETTERS
    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_author(self):
        return self.author

    def get_category(self):
        return self.category

    def get_tags(self):
        return self.tags

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    # METHODS
    def display_tags(self):
        return ', '.join(tag.name for tag in self.tags.all()[:3])

    def display_tags_count(self):
        return self.tags.count()

    def display_comments_count(self):
        return self.comments.count()

    def display_all_author_posts(self, author):
        return self.objects.filter(author=author)

    def display_all_posts_by_category(self, category):
        return self.objects.filter(category=category)

    def display_all_posts_by_tag(self, tag):
        return self.objects.filter(tags=tag)

    def display_all_posts_by_date(self, date):
        return self.objects.filter(created_at=date)

    def display_all_posts_by_month(self, month):
        return self.objects.filter(created_at__month=month)

    def display_all_posts_by_year(self, year):
        return self.objects.filter(created_at__year=year)
