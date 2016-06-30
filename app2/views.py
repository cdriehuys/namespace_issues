from django.core.urlresolvers import reverse

from django.http import HttpResponse


def index_view(request):
    """ Index view for app1 """
    response = HttpResponse()
    response.write('<p>This is the index view for app2</p>')

    url = reverse('index')

    response.write('<p>My url is: {}'.format(url))

    return response
