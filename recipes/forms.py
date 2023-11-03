from django import forms
from .models import UserBook



class RegistrationForm(forms.Form):

    username = forms.CharField(label='Username', max_length=100)

    email = forms.EmailField(label='Email')

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


class SavePageForm(forms.Form):

    user_book = forms.ModelChoiceField(queryset=UserBook.objects.all(), empty_label=None, label="Select User Book")