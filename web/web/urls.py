"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
# from django.views.generic import ListView, DetailView
# from bookmark.models import Bookmark
# from bookmark.views import BookmarkLV, BookmarkDV
from web.views import HomeView  # 홈 뷰 등록

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),  # 홈 뷰 추가
    path('bookmark/', include('bookmark.urls',), name='bookmark'),
    path('blog/', include('blog.urls',), name='blog'),
    path('polls/', include('polls.urls',), name='polls'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]