# Generated by Django 2.2.7 on 2020-01-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0008_auto_20200106_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='comment',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='civilstatus',
            field=models.CharField(choices=[('ledig', 'ledig'), ('verheiratet', 'verheiratet'), ('verwitwet', 'verwitwet'), ('in eingetragener Partnerschaft', 'in eingetragener Partnerschaft'), ('geschieden', 'geschieden'), ('gerichtlich getrennt', 'gerichtlich getrennt'), ('aufgelöste Partnerschaft', 'aufgelöste Partnerschaft')], default=None, max_length=100, null=True, verbose_name='Zivilstatus'),
        ),
    ]
