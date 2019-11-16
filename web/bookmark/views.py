from django.shortcuts import render
# generic 의 기존 view를 상속받음
from django.views.generic import ListView, DetailView
from .models import Bookmark
from django.http import HttpResponse


class BookmarkLV(ListView):
    model = Bookmark


class BookmarkDV(DetailView):
    model = Bookmark

#
# def index(request):
#     return HttpResponse("Hello, world. You're at the 북마크 index.")