# Generated by Django 4.2.6 on 2023-11-03 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ITCapp', '0002_user_age_user_city_user_country_user_email_user_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='country',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='state',
        ),
    ]
