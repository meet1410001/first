from django import forms
from django.contrib.auth.models import User
from captcha.fields import ReCaptchaField

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User  # Use the default Django User model
        fields = ['username', 'password', 'first_name', 'email']  # Add other fields as needed

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already in use. Please choose a different one.')
        return username
