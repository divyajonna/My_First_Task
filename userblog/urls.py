from django.conf.urls import url
from . import views

urlpatterns = [


    url(r'^signup/$', views.signup, name='signup'),

    #url(r'^$', views.post_list, name='post_list'),
]
