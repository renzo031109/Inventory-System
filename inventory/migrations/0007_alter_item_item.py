# Generated by Django 5.0.1 on 2024-06-09 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_item_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.itemdetails'),
        ),
    ]
