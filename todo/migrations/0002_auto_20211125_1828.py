# Generated by Django 3.2.9 on 2021-11-25 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated_at',
        ),
    ]
