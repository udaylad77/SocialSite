# 'get_user_model' will return 'User Model'.
# 'UserCreationForm' provide a built in form for create an user.

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    """
    Create a 'UserCreateForm' class for Registration and it's inherit from 'UserCreationForm'.
    """

    class Meta:
        """
        create a 'Meta' class, i want these are the fields from user to be able to access.
        """
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a custom Label for particular fields.
        # Takes two fields because i need to access later on for display.
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'Email address'
