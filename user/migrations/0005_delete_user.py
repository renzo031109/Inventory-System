# Generated by Django 5.0.1 on 2024-06-29 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
