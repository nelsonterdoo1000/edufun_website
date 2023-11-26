# Generated by Django 4.2.7 on 2023-11-15 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_trainee_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainee',
            name='message',
        ),
        migrations.AddField(
            model_name='trainee',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='trainee',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
