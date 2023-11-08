from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
    """
    This class defines a user registration form for signing up.

    :param forms.Form: The base form class.
    :type forms.Form: django.forms.Form

    :ivar username: The desired username for registration.
    :vartype username: str
    :ivar password: The password for the new user.
    :vartype password: str
    :ivar first_name: The first name of the user.
    :vartype first_name: str

    :cvar username: The username entered during registration.
    :vartype username: str

    :methods:
        - clean_username: Check if the username is already taken.
        - save: Save the user to the database after registration.
    """

    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100)

    def clean_username(self):
        """
        Check if the username is already taken.

        :param self: The SignUpForm object.
        :type self: SignUpForm

        :return: The username if it is available.
        :rtype: str

        :raises ValidationError: If the username is already taken.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists. Please choose a different username or log in.")
        return username

    def save(self):
        """
        Save the user to the database after sign up.

        :param self: The SignUpForm object.
        :type self: SignUpForm

        :return: The created user object.
        :rtype: User
        """
        user = User.objects.create_user(
            self.cleaned_data['username'],
            None,
            self.cleaned_data['password']
        )
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user
