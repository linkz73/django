from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from .models import Post


class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'  # 템플릿 이름을 수동으로 설정
    paginate_by = 2  # 한페이지에 2줄
    context_object_name = 'posts'  # 메타에서 사용. tamplates 에서 이름 사용 / object list 대신 사용 가능


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True


class PostMAV(MonthArchiveView):
    model = Post
    month_format = '%m'  # 추가
    date_field = 'modify_date'


class PostDAV(DayArchiveView):
    model = Post
    month_format = '%m'
    day_format = '%d'
    date_field = 'modify_date'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'
