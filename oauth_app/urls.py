from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from oauth_app import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="oauth_app/index.html")),
    path('accounts/', include('allauth.urls')),
    url(r'^logged_in/$', views.logged_in, name='logged_in'),
]