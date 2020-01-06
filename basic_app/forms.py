from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        help_texts = {
            'username': 'Bitte einen Kontonamen wählen (z.B. sonja.kistler)',
        }
        fields = ('username','email','password')



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        #fields = ('fname', 'fname', 'lname', 'street', 'zip', 'city', 'nationality', 'bday', 'ahvnumber', 'children', 'favorite_fruit')
        fields = (  'fname', 'fname', 'lname', 'street', 'zip', 'city', 'nationality', 'bday', 'tel',
                    'ahvnumber', 'children', 'civilstatus', 'zulage_fam',
                    'iban', 'bic')
