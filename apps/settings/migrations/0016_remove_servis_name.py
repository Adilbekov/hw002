# Generated by Django 5.0 on 2023-12-16 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0015_alter_servis_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servis',
            name='name',
        ),
    ]
