from django.urls import path
from . import views
from .views import *

app_name = 'bookmark'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', BookmarkLV.as_view(model=Bookmark), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(model=Bookmark), name='detail'),
    path('add/', BookmarkCreateView.as_view(model=Bookmark), name='add'),
    path('change/', BookmarkChangeLV.as_view(model=Bookmark), name='change'),
    path('<int:pk>/update/', BookmarkUpdateView.as_view(model=Bookmark), name='update'),
    path('<int:pk>/delete/', BookmarkDeleteView.as_view(model=Bookmark), name='delete'),
]