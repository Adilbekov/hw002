# Generated by Django 5.0 on 2023-12-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0023_blogpost_alter_newsletter_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя видео')),
                ('title', models.CharField(max_length=255, verbose_name='Пред заголовок')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('you_tube', models.URLField(verbose_name='URL-видео')),
            ],
        ),
    ]
