from django.core.urls import url

from app2 import views


urlpatterns = [
    url(r'^index/$', views.index_view, name='index'),
]
