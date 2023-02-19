from django.contrib.auth.models import User
from .models import NewContent
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, EmailInput, PasswordInput, CharField, EmailField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django import forms

class CreateForm(ModelForm):
    class Meta:
        model = NewContent
        fields = ['product', 'price', 'autor', 'description', 'date_of_publication']

        widgets = {
            'product': TextInput(attrs={'class': 'form-control','placeholder': 'Продукт'}),
            'price': TextInput(attrs={'class': 'form-control','placeholder': 'цена'}),
            'autor': TextInput(attrs={'class': 'form-control','placeholder': 'автор'}),
            'description': Textarea(attrs={'class': 'form-control','placeholder': 'описание'}),
            'date_of_publication': DateTimeInput(attrs={'class': 'form-control','type':'datetime-local','placeholder': 'дата'}),
        }


class SignUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control','placeholder': 'last_name'}),
            'email': EmailInput(attrs={'class': 'form-control','placeholder': 'email'}),

        }

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))

class SearchForm(ModelForm):
    product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'product'}))
    min_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'min_price'}))
    max_price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'max_price'}))

    class Meta:
        model = NewContent
        fields = ['product', 'min_price', 'max_price']




