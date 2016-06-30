from django.conf.urls import url

from app2 import views


# Setting app_name allows lookups like 'app2:index' to succeed even if
# the namespace is something else entirely.

app_name = 'app2'

urlpatterns = [
    url(r'^index/$', views.index_view, name='index'),
]
