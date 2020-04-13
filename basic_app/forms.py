from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from django.forms import ModelForm



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Bitte ein Passwort wählen und merken'}
                        ))

    class Meta():
        model = User
        help_texts = {
            'username': '',
        }

        fields = ('username','email','password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Bitte einen Kontonamen wählen (z.B. sonja_kistler85)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Ihre E-Mail Adresse'}),
            #'password': forms.TextInput(attrs={'class': 'form-control'}),
            #'password': forms.PasswordInput(attrs={'class': 'form-control input-lg',
            #                                        'placeholder': 'Passwort bitte merken'
            #                                        }),
                }


class UserProfileInfoForm(forms.ModelForm):

    #nationality = forms.CharField(widget=forms.TextInput(attrs={'class': 'bootstrap-select'}))
    #nationality = forms.CharField(widget=forms.TextInput(attrs={'class': 'regDropDown'}))
    #nationality =

    class Meta():
        model = UserProfileInfo
        #fields = ('fname', 'fname', 'lname', 'street', 'zip', 'city', 'nationality', 'bday', 'ahvnumber', 'children', 'favorite_fruit')
        fields = (  'fname', 'lname', 'street', 'zip', 'city', 'nationality', 'bday', 'tel',
                    'ahvnumber', 'civilstatus', 'zulage_fam', 'children',
                    'iban', 'bank', 'notfall_name', 'notfall_tel', 'notfall_wohnort')




        widgets = {

            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            #'nationality': forms.TextInput(attrs={'class': 'select'}),

            'bday': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'ahvnumber': forms.TextInput(attrs={'class': 'form-control'}),
            'children': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            #'civilstatus': forms.TextInput(attrs={'class': 'form-control'}),
            'iban': forms.TextInput(attrs={'class': 'form-control'}),
            'bank': forms.TextInput(attrs={'class': 'form-control'}),
            'notfall_name': forms.TextInput(attrs={'class': 'form-control'}),
            'notfall_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'notfall_wohnort': forms.TextInput(attrs={'class': 'form-control'}),

            'zulage_fam': forms.TextInput(attrs={'class': 'form-control', 'style': 'narrow-select'}),


			}
