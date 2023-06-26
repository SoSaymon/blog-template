from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])
