# Generated by Django 3.0.4 on 2020-04-04 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peinture', '0011_peinture_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peinture',
            name='style',
        ),
    ]
