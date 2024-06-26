# Generated by Django 5.0.1 on 2024-06-29 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, null=True)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['uom'],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('remarks', models.CharField(max_length=50, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('uom', models.CharField(max_length=20, null=True)),
                ('item_name', models.CharField(blank=True, max_length=200, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=200, null=True)),
                ('staff_name', models.CharField(blank=True, max_length=100, null=True)),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.client')),
                ('department_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.department')),
                ('item_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.itemcode')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='ItemBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200, null=True)),
                ('brand_name', models.CharField(max_length=200, null=True)),
                ('soh', models.IntegerField(null=True)),
                ('item_code', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(max_length=50, null=True)),
                ('uom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.uom')),
            ],
            options={
                'ordering': ['item_name'],
            },
        ),
    ]
