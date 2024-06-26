# Generated by Django 5.0.4 on 2024-04-28 17:30

import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=myapp.models.get_current_date),
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
