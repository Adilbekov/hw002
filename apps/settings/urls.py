# from django.urls import path
# from apps.settings.views import index

# urlpatterns = [
#     path('', index,name='index')
# ]

from django.urls import path
from apps.settings.views import index_1

urlpatterns = [
    path('', index_1, name= 'index_1'),
]