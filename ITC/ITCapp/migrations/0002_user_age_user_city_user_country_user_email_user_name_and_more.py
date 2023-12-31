# Generated by Django 4.2.6 on 2023-11-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITCapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=22, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
