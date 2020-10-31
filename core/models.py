from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Core(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core')
    slug = models.SlugField(max_length=200, unique=True)
    updated = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        """
        docstring
        """
        return reverse('core:single', args=[self.slug])

    class Meta:
        """
        docstring
        """
        ordering = ['-published']

    def __str__(self):
        """
        docstring
        """
        return self.title