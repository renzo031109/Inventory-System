# Generated by Django 5.0.1 on 2024-05-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetails',
            name='brand_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]