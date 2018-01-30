from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views as core_views

urlpatterns = [


    url(r'^signup/$', core_views.signup, name='signup'),
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', core_views.home, name='home'),

    url(r'^login/$', auth_views.login, {'template_name': 'userblog/login.html'}, name='login'),

    #publishing the post from models
    url(r'^posts$', core_views.userpost_list, name='userpost_list'),
    #added url for postdetails
    url(r'^posts/(?P<pk>\d+)/$', core_views.userpost_detail, name='userpost_detail'),

    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

]
