# Generated by Django 5.0.1 on 2024-05-22 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_item_options_alter_itemname_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemname',
            name='uom',
        ),
    ]
