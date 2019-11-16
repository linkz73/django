from django.views.generic.base import TemplateView
# base html : 공통 헤더 등


class HomeView(TemplateView):
    template_name = 'home.html'


