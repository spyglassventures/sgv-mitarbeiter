# Generated by Django 2.2.7 on 2020-01-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20200106_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='zulage_fam',
            field=models.CharField(default='SOME STRING', max_length=140),
        ),
    ]
