# Generated by Django 3.0.1 on 2021-11-29 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0007_auto_20211129_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sort_term_memory',
            name='correct_rate',
            field=models.IntegerField(),
        ),
    ]
