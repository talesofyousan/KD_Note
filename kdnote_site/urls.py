from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
	url(r'^mypage/$', views.mypage, name="mypage")
]