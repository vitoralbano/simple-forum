from django.urls import path

from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.BoardsIndexView.as_view(), name='index')
]
