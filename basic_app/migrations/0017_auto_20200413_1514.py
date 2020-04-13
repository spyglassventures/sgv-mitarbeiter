# Generated by Django 2.2.7 on 2020-04-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0016_auto_20200121_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, verbose_name='Frei waehlbarer Benutzername')),
                ('email', models.CharField(max_length=25, verbose_name='E-Mail Adresse')),
                ('password', models.CharField(max_length=25, verbose_name='Passwort')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='children',
            field=models.TextField(max_length=225, verbose_name='Angaben zu Ihren Kindern, sofern vorhanden (Name & Geburtsdatum, bis 25 Jahre)'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='nationality',
            field=models.CharField(choices=[('Schweiz', 'Schweiz'), ('Deutsch', 'Deutsch'), ('Italien', 'Italien'), ('Andere', 'Andere'), ('----', '---------'), ('Kosovo', 'Kosovo'), ('Serbien', 'Serbien')], default=None, max_length=100, null=True, verbose_name='Nationalität'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='notfall_name',
            field=models.CharField(default='Vorname, Nachname (z.B. von Eltern, Partner/-in)', help_text='', max_length=45, verbose_name='Notfallkontakt'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='notfall_tel',
            field=models.CharField(default='', max_length=25, verbose_name='Telefon des Notfallkontaktes'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='notfall_wohnort',
            field=models.CharField(default='', max_length=25, verbose_name='Wohnort des Notfallkontaktes'),
        ),
    ]
