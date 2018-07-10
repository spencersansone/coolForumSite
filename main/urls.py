from . import views
from django.conf.urls import url

app_name = 'main'

urlpatterns = [
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^profile/$', views.profile, name='profile'),
]