from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from validate_email import validate_email


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        xxx = validate_email(str(email),verify=True)
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        elif "@gmail.com" not in email:   
            raise forms.ValidationError("Register with IITD IDs with domain only '@iitd.ac.in'") 
        elif xxx==False:
                raise forms.ValidationError("Invalid email")
        elif(xxx==None):
            raise forms.ValidationError("Invalid Email Address")        
        return email    
        

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']