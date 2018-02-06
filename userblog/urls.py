from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views as core_views

from django.contrib import admin

urlpatterns = [

    url(r'^admin/',admin.site.urls),

    url(r'^signup/$', core_views.signup, name='signup'),
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', core_views.home, name='home'),

    url(r'^login/$', auth_views.login, {'template_name': 'userblog/login.html'}, name='login'),

    #publishing the post from models
    url(r'^posts$', core_views.userpost_list, name='userpost_list'),
    #added url for postdetails
    url(r'^posts/(?P<pk>\d+)/$', core_views.userpost_detail, name='userpost_detail'),
    #adding postnew
    url(r'^posts/new/$', core_views.userpost_new, name='userpost_new'),
    #to enable edditing to the post we created
    url(r'^posts/(?P<pk>\d+)/edit/$', core_views.userpost_edit, name='userpost_edit'),

    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),

]
