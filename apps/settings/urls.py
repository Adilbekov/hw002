# from django.urls import path
# from apps.settings.views import index

# urlpatterns = [
#     path('', index,name='index')
# ]

from django.urls import path
from apps.settings.views import index_1, index_2, index_3

urlpatterns = [
    path('', index_1, name= 'index_1'),
    path('blog-post.html', index_2, name= 'index_2'),
    path('blog.html', index_3, name= 'index_3')
]