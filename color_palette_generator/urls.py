from django.urls import path
from . import views #viewsにあるすべてを持ってくる

urlpatterns = [
    path('', views.index, name='index'),
]

