from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.homepg,name='homepg'),
    url(r'^send_msg/$',views.send_msg,name='send_msg'),
    url(r'^play_audio/$',views.play_audio,name='play_audio'),
]
