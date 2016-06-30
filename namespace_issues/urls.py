from django.conf.urls import include, url

# app_name can be specified in the include() call, but that is
# deprecated, so it's better to put it in the urls.py file for the app

urlpatterns = [
    url(r'^app1/', include('app1.urls', app_name='app1', namespace='non-app-name')),
    url(r'^app2/', include('app2.urls', namespace='random')),
]
