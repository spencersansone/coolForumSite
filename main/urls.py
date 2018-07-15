from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

app_name = 'main'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^addPost/$', views.addPost, name='add_post'),
    url(r'^posts/(?P<pk>[0-9]+)/$', login_required(views.postDetail.as_view()), name='postDetail'),
    url(r'^verificationCode/$', views.verificationCode, name='verification_code'),
    url(r'^resendVerificationCode/$', views.resendVerificationCode, name='resend_verification_code'),
]