# Generated by Django 4.1.3 on 2022-12-16 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='roomname',
            new_name='name',
        ),
    ]