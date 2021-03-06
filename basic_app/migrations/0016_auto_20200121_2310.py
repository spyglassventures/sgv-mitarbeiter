# Generated by Django 2.2.7 on 2020-01-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0015_auto_20200121_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='notfall_name',
            field=models.CharField(default='Vorname, Nachname', help_text='(z.B. Eltern, Partner/-in', max_length=45, verbose_name='Notfallkontakt'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='notfall_tel',
            field=models.CharField(default='', max_length=25, verbose_name='Telefon Notfallkontakt'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='notfall_wohnort',
            field=models.CharField(default='', max_length=25, verbose_name='Wohnort des Notfallkontakt'),
        ),
    ]
