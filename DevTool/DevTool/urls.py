from django.conf.urls import include, url
import DevToolApp.views

# Django processes URL patterns in the order they appear in the array
# r 접두사 "원시" 문자열 내의 문자를 이스케이프하지 않도록 지시
# ^ "줄의 시작 / $ "줄의 끝"
urlpatterns = [
    url(r'^$', DevToolApp.views.index, name='index'),
    url(r'^home$', DevToolApp.views.index, name='home'),
    url(r'^about$', DevToolApp.views.about, name='about'),
]