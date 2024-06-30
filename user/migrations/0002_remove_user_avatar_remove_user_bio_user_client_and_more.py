# Generated by Django 5.0.1 on 2024-06-29 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.AddField(
            model_name='user',
            name='client',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.TextField(max_length=200, null=True),
        ),
    ]