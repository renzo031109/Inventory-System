# Generated by Django 5.0.1 on 2024-06-09 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_itemdetails_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='remarks',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
