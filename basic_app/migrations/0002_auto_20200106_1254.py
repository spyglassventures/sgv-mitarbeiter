# Generated by Django 2.2.7 on 2020-01-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='ahvnumber',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='bday',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='children',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='city',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='fname',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='lname',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='nationality',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='street',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='zip',
            field=models.URLField(blank=True),
        ),
    ]
