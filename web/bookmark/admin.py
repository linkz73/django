from django.contrib import admin
from .models import Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


# admin 관리자 페이지에 BookmarkAdmin 을 추가해 줌.
admin.site.register(Bookmark, BookmarkAdmin)
