# Generated by Django 3.0.2 on 2020-01-23 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ColumbiaApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='cusine',
            new_name='cuisine',
        ),
    ]
