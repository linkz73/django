from django.urls import path
from . import views
from .views import *

app_name = 'bookmark'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', BookmarkLV.as_view(model=Bookmark), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(model=Bookmark), name='detail'),
]