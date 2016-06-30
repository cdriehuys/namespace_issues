from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    """ Index view for app2 """
    context = {}

    # Calls to reverse() should use the 'app_name' as the namespace.
    # 'app_name' is defined in urls.py

    app1_url = reverse('app1:index')
    context['app1_url'] = app1_url

    app2_url = reverse('app2:index')
    context['app2_url'] = app2_url

    return render(request, 'app2/index.html', context)
