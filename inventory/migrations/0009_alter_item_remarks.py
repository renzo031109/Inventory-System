# Generated by Django 5.0.1 on 2024-05-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_item_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='remarks',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
