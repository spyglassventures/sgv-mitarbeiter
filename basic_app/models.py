from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.safestring import mark_safe

# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

# Defince choices for radio buttons:
CIVIL= [
    ('ledig', 'ledig'),
    ('verheiratet', 'verheiratet'),
    ('verwitwet', 'verwitwet'),
    ('in eingetragener Partnerschaft', 'in eingetragener Partnerschaft'),
    ('geschieden', 'geschieden'),
    ('gerichtlich getrennt', 'gerichtlich getrennt'),
    ('aufgelöste Partnerschaft', 'aufgelöste Partnerschaft'),
    ]


NAT= [
    ('Schweiz', 'Schweiz'),
    ('Deutsch', 'Deutsch'),
    ('Italien', 'Italien'),
    ('Andere', 'Andere'),
    ('----', '---------'),
    ('Kosovo', 'Kosovo'),
    ('Serbien', 'Serbien'),
    ]

class UserForm(models.Model):
    username = models.CharField(max_length=25, verbose_name='Frei waehlbarer Benutzername')
    email = models.CharField(max_length=25, verbose_name='E-Mail Adresse')
    password = models.CharField(max_length=25, verbose_name='Passwort')



    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


# Create your models here.
class UserProfileInfo(models.Model):


    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    #portfolio_site = models.URLField(blank=True)
    #username = models.CharField(max_length=255, verbose_name='Frei wählbarer Nutzername')
    #email = models.CharField(max_length=255, verbose_name='E-Mail')
    #password = models.CharField(max_length=255, verbose_name='Passwort')

    fname = models.CharField(max_length=25, verbose_name='Vorname')
    lname = models.CharField(max_length=25, verbose_name='Nachname')
    street = models.CharField(max_length=25, verbose_name='Strasse')
    zip = models.CharField(max_length=25, verbose_name='Postleitzahl')
    city = models.CharField(max_length=25, verbose_name='Stadt')
    #nationality = models.CharField(max_length=25, verbose_name='Nationalität')
    bday = models.CharField(max_length=25, verbose_name='Geburtstag')
    tel = models.CharField(max_length=25, default='+41', verbose_name='Telefonnummer')
    ahvnumber = models.CharField(max_length=25, default='756.XXXX.XXXX.XX', verbose_name='AHV-Nummer')
    zulage_fam = models.CharField(max_length=140, default='ja/nein', verbose_name='Beantragen Sie Familienzulagen? Falls ja, ab wann?')
    children = models.TextField(max_length=225, verbose_name='Angaben zu Ihren Kindern, sofern vorhanden (Name & Geburtsdatum, bis 25 Jahre)') # WORKS
    iban = models.CharField(max_length=25, default='CH...', verbose_name='Ihre IBAN Nummer')
    bank = models.CharField(max_length=25, default='', verbose_name='Name der Bank')
    notfall_name = models.CharField(max_length=45, default='Vorname, Nachname (z.B. von Eltern, Partner/-in)', verbose_name='Notfallkontakt', help_text=mark_safe("")) #help_text='(z.B. Eltern, Partner/-in')
    notfall_tel = models.CharField(max_length=25, default='', verbose_name='Telefon des Notfallkontaktes')
    notfall_wohnort = models.CharField(max_length=25, default='', verbose_name='Wohnort des Notfallkontaktes')


    # children = models.CharField(widget=models.Textarea) # TODO

    nationality = models.CharField(
        null=True, max_length=100, # maximal length of integers provided
        default=None,
        choices=NAT,
        #selected = 'Schweiz',
        #attrs='',
        #choices=NAT(label='', choices=NAT, widget=forms.Select(attrs={'class':'regDropDown'})),
        #widget=forms.Select(attrs={'class':'regDropDown'}),
        verbose_name='Nationalität')

    civilstatus = models.CharField(
        null=True, max_length=100, # maximal length of integers provided
        default=None,
        choices=CIVIL, verbose_name='Zivilstatus')
    #favorite_fruit = models.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES)) # MW
    #comment = forms.CharField(widget=forms.Textarea)   #NW


    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    #profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
