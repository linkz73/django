from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# 1,3번 설정으로 python2 환경에서도 보이게 함.


@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    # 필드명=models.데이터타입(제약조건=값, ...)
    url = models.URLField('url', unique=True)

    def __str__(self):  # __str__ 메서드는 객체명만 사용할때 주소 리턶는 것을 특정 문자열로 반환.
        return self.title
