# Generated by Django 5.0 on 2023-12-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_yourmodel_our_discriptions_3_our_title_3'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ваше имя')),
                ('descriptions', models.TextField(verbose_name='Описание к вам')),
                ('title_1', models.CharField(max_length=255, verbose_name='Заголовок для информации')),
                ('discriptions_1', models.TextField(verbose_name='Описание для информации')),
                ('title_2', models.CharField(max_length=255, verbose_name='Дополнительный заголовок для информации')),
                ('discriptions_2', models.TextField(verbose_name='Дополнительная информация')),
                ('title_3', models.CharField(max_length=255, verbose_name='Дп. заголовок для информации')),
                ('discriptions_3', models.TextField(verbose_name='Дп. информация')),
                ('botton', models.CharField(max_length=50, verbose_name='Название кнопки')),
                ('image', models.ImageField(upload_to='', verbose_name='ваше фото')),
            ],
            options={
                'verbose_name': 'Наша информация',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.DeleteModel(
            name='Our',
        ),
    ]