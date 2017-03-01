from django.conf.urls import url
from usuarios import views
from django.contrib.auth import views as dviews

urlpatterns = [
    url(r'^registrar/$', views.RegistrarUsuarioView.as_view(), name="registrar"),
    url(r'^login/$', dviews.login, {'template_name' : 'login.html'}, name='login'),
    url(r'^logout/$', dviews.logout_then_login, {'login_url': '/login/'}, name='logout')
]