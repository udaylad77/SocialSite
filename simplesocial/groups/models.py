# 'slugify' :- Convert spaces or repeated dashes to single dashes.
#   Remove characters that aren't alphanumerics, underscores, or hyphens.
#   Convert to lowercase.

# 'misaka' :- Fast HTML renderer and functionality to make custom renderers.

from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()


# GROUPS MODELS.PY FILE
# Create your models here.


class Group(models.Model):
    """
    For storing Group details in model.
    """
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=True, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = self.description
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    """
    For storing Group Members in model.
    """
    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')