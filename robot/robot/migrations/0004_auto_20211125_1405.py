# Generated by Django 3.0.1 on 2021-11-25 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0003_auto_20211123_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sort_term_memory',
            name='three',
        ),
        migrations.RemoveField(
            model_name='sort_term_memory',
            name='two',
        ),
        migrations.RemoveField(
            model_name='timestore',
            name='time_three',
        ),
        migrations.RemoveField(
            model_name='timestore',
            name='time_two',
        ),
    ]
