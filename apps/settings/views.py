from django.shortcuts import render
from apps.settings import models
# Create your views here.


def index_1(requests):
    slide=models.MainPage.objects.all()
    about_us=models.AboutUs.objects.latest('id')
    personal_info=models.PersonalInformation.objects.latest('id')
    servis=models.Servis.objects.all()
    reviewss=models.Reviews.objects.all()
    portfolio=models.Partfolio.objects.all()
    facts=models.Facts.objects.all()
    comands=models.OurTeam.objects.all()
    news=models.Newsletter.objects.latest('id')
    blog_post=models.BlogPost.objects.all()
    video=models.Video.objects.latest('id')
    info=models.InfoContacts.objects.latest('id')
    ass=models.Ass.objects.latest('id')
    logo=models.HomeLogo.objects.latest('id')
    return render(requests, 'index-kenburns.html', locals())

# def index(requesrt):
