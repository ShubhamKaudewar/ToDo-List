# Generated by Django 3.0.7 on 2020-07-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodel',
            name='noteValue',
            field=models.TextField(blank=True, null=True),
        ),
    ]
