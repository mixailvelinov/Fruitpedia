from django import forms

from profiles.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['image', 'age']

        labels = {
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': ''
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),

        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['email', 'password']

