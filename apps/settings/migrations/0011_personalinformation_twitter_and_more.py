# Generated by Django 5.0 on 2023-12-16 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0010_alter_personalinformation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='twitter',
            field=models.URLField(default=1, verbose_name='Твиттер'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='mini_description',
            field=models.TextField(verbose_name='Предописание'),
        ),
    ]
