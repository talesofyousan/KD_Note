from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.login_phase, name='login'),
	url(r'^mypage/$', views.mypage, name="mypage"),
]