from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

from .models import Board


class BoardsIndexView(generic.ListView):
    template_name = 'boards/index.html'
    context_object_name = 'boards'

    def get_queryset(self):
        return Board.objects.all()
