from django.urls import re_path
from teamwork import views

urlpatterns = [
    re_path(r'^account/$', views.account, name='account'),
    re_path(r'^settings/$', views.settings, name='settings'),
    re_path(r'^notifications/$', views.notifications, name='notifications'),
    re_path(r'^colleagues/$', views.colleagues, name='colleagues'),
    re_path(r'^meetings/$', views.meetings, name='meetings'),
    re_path(r'^tasks/$', views.tasks, name='tasks'),
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^authorization/$', views.authorization, name='authorization'),
    re_path(r'^registration/$', views.registration, name='registration'),
    re_path(r'^logout/$', views.doLogout, name='logout'),
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^task/$', views.task, name='task')
]