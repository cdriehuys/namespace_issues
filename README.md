# Django Namespace Issues

### The Problem

I was having troubles with using namespaces along with reusable apps. For details, see [this stackoverflow question](http://stackoverflow.com/questions/38060270/how-to-deal-with-namespacing-urls-in-a-reusable-django-app).


### The Solution

As the [Django docs on URL resolution](https://docs.djangoproject.com/en/1.9/topics/http/urls/#topics-http-reversing-url-namespaces) state, Django first looks for a matching application namespace. We can use this by defining an `app_name` in our urls.py file.

```python
# myapp/urls.py

app_name = 'myapp'

urlpatterns = [
    ...
    url(r'^index', IndexView.as_view(), name='index'),
    ...
]
```

Even if the app is included in a project like so:

```python
# project/urls.py

urlpatterns = [
    url(r'^myapp/', include('myapp.urls', namespace='random-namespace')),
]
```

...the urls are still accessible through `reverse('myapp:index')` because of the `app_name` property.