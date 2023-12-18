from django.db import models

# Create your models here.

class MainPage(models.Model):
    image=models.ImageField(
    upload_to='main_image_user',
    verbose_name='Фотография'
    )
    title=models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    desctiptions=models.CharField(
        verbose_name='Описание',
        max_length=255
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Слайд'
        verbose_name_plural='Слайды'


class AboutUs(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Ваше имя'
    )
    descriptions=models.TextField(
        verbose_name='Описание к вам'
    )
    title_1=models.CharField(
        max_length=255,
        verbose_name='Первый заголовок'
    )
    discriptions_1=models.TextField(
        verbose_name='Первое описание'
    )
    title_2=models.CharField(
        max_length=255,
        verbose_name='Второй заголовок'
    )
    discriptions_2=models.TextField(
        verbose_name='Второе описание'
    )
    title_3=models.CharField(
        max_length=255,
        verbose_name='Третий заголовок'
    )
    discriptions_3=models.TextField(
        verbose_name='Третее описание'
    )
    botton=models.CharField(
        max_length=50,
        verbose_name='Название кнопки'
    )
    image=models.ImageField(
        upload_to='user_image',
        verbose_name='ваше фото'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Наша информация'
        verbose_name_plural='О нас'



class PersonalInformation(models.Model):
    profession=models.CharField(
        max_length=255,
        verbose_name='Профессия'
    )
    name=models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    mini_description=models.TextField(
        verbose_name='Предописание'
    )
    description=models.TextField(
        verbose_name='Описание'
    )
    image=models.ImageField(
        upload_to='personal_userimage',
        verbose_name='Фотография'
    )
    twitter=models.URLField(
        verbose_name='URL-Твиттер'
    )
    facebook=models.URLField(
    verbose_name='URL-Facebook'
    )
    skype=models.URLField(
    verbose_name='URL-skype'
    )
    instagramm=models.URLField(
    verbose_name='URL-Инстаграм'
    )
    inn=models.URLField(
    verbose_name='URL-In'
    )
    you_tube=models.URLField(
    verbose_name='URL-You Tube'
    )

    def __str__(self):
        return f'{self.name} - {self.profession}'
    
    class Meta():
        verbose_name='Ваша информация'
        verbose_name_plural='Личная информация'



class Servis(models.Model):
    title=models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    descriptions=models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Наши сервисы'
        verbose_name_plural='Наш сервис'
              
        
class Reviews(models.Model):
    user_image=models.ImageField(
        verbose_name='Фото клиента',
        upload_to='user_photo'
    )
    reviews=models.TextField(
        max_length=255,
        verbose_name='Отзыв'
    )
    name=models.CharField(
        max_length=255,
         verbose_name='Имя'
    )
    profession=models.CharField(
        max_length=255,
        verbose_name='Професия'
    )

    def __str__(self):
        return f"{self.name} - {self.profession}"
        
    class Meta:
        verbose_name='Отзывы'
        verbose_name_plural='Отзыв'

class Partfolio(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    descriptions=models.TextField(
        max_length=255,
        verbose_name='Описание'
    )
    image=models.ImageField(
        upload_to='partfolio_user_image',
        verbose_name='Фотография'
    )


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Портфолии'
        verbose_name_plural='Портфолио'

class Facts(models.Model):
    title=models.CharField(
        max_length=255,
        verbose_name='Балл'
    )
    descriptions=models.CharField(
        max_length=255,
        verbose_name='Название'
    )

    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name='Крутые факты'
        verbose_name_plural='Крутой факт'

class OurTeam(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Имя-фамилия'
    )
    profession=models.CharField(
        max_length=255,
        verbose_name='Професия'
    )
    image=models.ImageField(
        verbose_name='Фотография',
        upload_to='uorteam_user_image'
    )
    facebook=models.URLField(
        verbose_name='URL-Фейсбук'
    )
    twitter=models.URLField(
        verbose_name='URL-Твиттер'
    )
    google=models.URLField(
        verbose_name='URL-Google+'
    )

    def __str__(self):
        return f'{self.name} - {self.profession}'
    
    class Meta:
        verbose_name='Наши команды'
        verbose_name_plural='Наша команда'


class Newsletter(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    title=models.CharField(
        max_length=255,
        verbose_name='Пред описание'
    )
    title_2=models.TextField(
        verbose_name='Описание'
    )
    botton=models.CharField(
        max_length=255,
        verbose_name='Название кнопки'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Cвязаться с нами'
        verbose_name_plural='Обратная связ'


class BlogPost(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    description=models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image=models.ImageField(
        upload_to='blogpost_image',
        verbose_name='Фотография'
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank = True,null = True
    )
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Blog-публикации'
        verbose_name_plural='Blog-публикация'

class Video(models.Model):
    name=models.CharField(
        max_length=255,
        verbose_name='Имя видео'
    )
    title=models.CharField(
        max_length=255,
        verbose_name='Пред заголовок'
    )
    descriptions=models.TextField(
        verbose_name='Описание'
    )
    you_tube=models.URLField(
        verbose_name='URL-видео'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Видео'
        verbose_name_plural='Загруза видео'

class InfoContacts(models.Model):
    title_1=models.CharField(
        max_length=255,
        verbose_name='Заголовок для информации'
    )
    descriptions_1=models.CharField(
        max_length=255,
        verbose_name='Расписание рабочего дня'
    )
    descriptions111=models.CharField(
        max_length=255,
        verbose_name='Расписание рабочего дня'
    )
    descriptions1111=models.CharField(
        max_length=255,
        verbose_name='Расписание рабочего дня'
    )
    title_2=models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    descriptions_2=models.CharField(
        max_length=255,
        verbose_name='Контактная информация'
    )
    descriptions222=models.CharField(
        max_length=255,
        verbose_name='Контактная информация'
    )
    email=models.EmailField(
        verbose_name='email.com'
    )
    url=models.URLField(
        verbose_name='URL-почты'
    )
    def __str__(self):
        return f'{self.title_1} - {self.title_2}'
    
    class Meta:
        verbose_name='Информации о работе'
        verbose_name_plural='Информация о работе'


class Ass(models.Model):
    info=models.CharField(
        max_length=255,
        verbose_name='Не-много о компании'
    )
    razrab=models.URLField(
        verbose_name='Сылка для разработчика'
    )
    name_razrab=models.CharField(
        max_length=255,
        verbose_name='Имя разработчика'
    )
    twitter=models.URLField(
        verbose_name='URL-для твиттера'
    )
    facebook=models.URLField(
        verbose_name='URL-для фейсбука'
    )
    google=models.URLField(
        verbose_name='URL-для гугла'
    )
    skype=models.URLField(
        verbose_name='URL-для skype'
    )
    instagram=models.URLField(
        verbose_name='URL-для инстаграмма'
    )
    inn=models.URLField(
        verbose_name='URL-для Linkedin'
    )
    you_tube=models.URLField(
        verbose_name='URL-для You Tube'
    )
    
    def __str__(self):
        return self.info
    
    class Meta:
        verbose_name='Ass'
        verbose_name_plural='Ass'

class HomeLogo(models.Model):
    image=models.ImageField(
        verbose_name='Логотип',
        upload_to='logo_home'
    )
    
    class Meta:
        verbose_name='Логотипы'
        verbose_name_plural='Логотип'





# авто зополнение времени
        # created_add=models.DateTimeField(
        #     auto_now_add=True,
        #     blank=True, null=True
        # )