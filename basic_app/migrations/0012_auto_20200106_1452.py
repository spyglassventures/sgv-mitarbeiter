# Generated by Django 2.2.7 on 2020-01-06 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_auto_20200106_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='bic',
            field=models.CharField(default='', max_length=25, verbose_name='BIC Nummer Ihrer Bank'),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='iban',
            field=models.CharField(default='CH...', max_length=25, verbose_name='Ihre IBAN Nummer'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='ahvnumber',
            field=models.CharField(default='756.XXXX.XXXX.XX', max_length=25, verbose_name='AHV-Nummer'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='zulage_fam',
            field=models.CharField(default='ja/nein', max_length=140, verbose_name='Beantragen Sie Familienzulagen? Falls ja, ab wann?'),
        ),
    ]
