from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.Form):
    """
    This class will create a form for the user to sign up.
    Parameters:
        forms.form: form
    Attributes:
        username: str
        password: str
        first_name: str

    Methods:
        clean_username: This method will check if the username is already taken.
        save: This method will save the user to the database.
    """
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=100)


    def clean_username(self):
        """
        This method will check if the username is already taken.
        Parameters:
            self: SignUpForm object
        Returns:
            username: str
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("A user with this username already exists. Please choose a different username or login.")
        return username
    
    
    #save the user to the database
    def save(self):
        """
        This method will save the user to the database.
        Parameters:
            self: SignUpForm object
        Returns:
            None
        """
        user = User.objects.create_user(
            self.cleaned_data['username'],
            None,
            self.cleaned_data['password']
        )
        user.first_name = self.cleaned_data['first_name']
        user.save()
        return user