from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now)  # time zone datetime object?
    author = models.ForeignKey(      # WHat is foriegn key? # TODO:
        User, on_delete=models.CASCADE)  # Why ON cascade??

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
