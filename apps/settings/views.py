from django.shortcuts import render

# Create your views here.

# def index(requests):
#     return render(requests, )
def index_1(requests):
    return render(requests, 'index-kenburns.html', locals())


def index_2(requests):
    return render(requests, 'blog-post.html', locals())


def index_3(requests):
    return render(requests, 'blog.html', locals())