from django.db import models
from django.contrib import auth

# Display name - Uday
# email - uday@gmail.com
# password - Ud@yLad45

# Create your models here.


class User(auth.models.User, auth.models.PermissionsMixin):
    """
    Create a User class for Registration using django administration.
    """
    def __str__(self):
        """
        String representation.
        :return: - Registered username.
        """
        return "@{}".format(self.username)