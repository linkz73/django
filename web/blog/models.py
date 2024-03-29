from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from tagging.fields import TagField
# 1,3번 설정으로 python2 환경에서도 보이게 함.
from django.contrib.auth.models import User
from django.utils.text import slugify


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='제목을 위한 별칭으로 한개의 단어로 사용')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True)
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_date = models.DateTimeField('MODIFY DATE', auto_now=True)
    tag = TagField()
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'post'  # 이 이름을 이용해서 표시 가능
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
        # return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Post, self).save(*args, **kwargs)