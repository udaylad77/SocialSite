from django.contrib import admin
from . import models

# Register your models here.

# tabular inline class
# It's allow us to utilize the admin interface and out django website with the
# ability to edit models on the same page as the parent model


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)