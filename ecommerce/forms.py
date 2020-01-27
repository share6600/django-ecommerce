from django import forms
from django.contrib.auth import get_user_model

User= get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your full name"}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "your content"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "your content"}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "gmail.com" not in email:
            raise forms.ValidationError('email must be in gmail')
        return email
class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your username"}))        
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "your password"}))        

class RegisterForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "your username"}))
    email= forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "your username"})) 
    password= forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "your password"}))
    password2= forms.CharField(label='confirm password',widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "your password"}))
    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
           raise forms.ValidationError('the user you enterd is used already ')
        return username

    def clean_email(self):
        email=self.cleaned_data.get('username')
        qs=User.objects.filter(email=email)
        if qs.exists():
           raise forms.ValidationError('the email you enterd is taken ') 
        return email
    def clean(self):
        data=self.cleaned_data
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        email=self.cleaned_data.get('email')

        if password != password2:
            raise forms.ValidationError('your tow passwords not match ')
        else:
            return data