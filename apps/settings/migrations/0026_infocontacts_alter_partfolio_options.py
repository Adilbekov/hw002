# Generated by Django 5.0 on 2023-12-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0025_alter_video_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=255, verbose_name='Заголовок для информации')),
                ('descriptions_1', models.CharField(max_length=255, verbose_name='Расписание рабочего дня')),
                ('title_2', models.CharField(max_length=255, verbose_name='Название')),
                ('descriptions_2', models.TextField(verbose_name='Контактная информация')),
            ],
            options={
                'verbose_name': 'Информации о работе',
                'verbose_name_plural': 'Информация о работе',
            },
        ),
        migrations.AlterModelOptions(
            name='partfolio',
            options={'verbose_name': 'Портфолии', 'verbose_name_plural': 'Портфолио'},
        ),
    ]
