# from django.urls import path
# from apps.settings.views import index

# urlpatterns = [
#     path('', index,name='index')
# ]

from django.urls import path
from apps.settings import views

urlpatterns = [
    path('', views.index_1, name= 'index_1'),
    path('blog_post/<int:id>/', views.blog_post, name='blog_postt'),
    path('blog', views.blog, name='blog')
]