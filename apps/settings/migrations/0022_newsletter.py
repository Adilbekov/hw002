# Generated by Django 5.0 on 2023-12-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0021_ourteam_alter_personalinformation_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('title', models.CharField(max_length=255, verbose_name='Пред описание')),
                ('title_2', models.TextField(verbose_name='Описание')),
                ('botton', models.CharField(max_length=255, verbose_name='Название кнопки')),
            ],
            options={
                'verbose_name': 'Cвязаться с нами',
                'verbose_name_plural': 'Обратная связь',
            },
        ),
    ]