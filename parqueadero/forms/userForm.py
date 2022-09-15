from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class admin(UserCreationForm):
    username = forms.CharField(label="Username", required=True, max_length=25,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    email = forms.CharField(label="Email", required=True, max_length=45,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter email', 'type': 'email'}))
    password1 = forms.CharField(label="Password", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter password', 'type': 'password'}))
    password2 = forms.CharField(label="Confirm password", required=True, max_length=25,
                                widget=forms.TextInput(attrs={'placeholder': 'Confirm password', 'type': 'password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        help_texts = {k: "" for k in fields}


'''class superUser(UserCreationForm):
    email = forms.CharField(label="Email", required=True, max_length=25,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter your email', 'type': 'email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'is_superuser',
            'is_staff',
        ]
        help_texts = {k: "" for k in fields}'''
