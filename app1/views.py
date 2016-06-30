from django.http import HttpResponse


def index_view(request):
    """ Index view for app1 """
    return HttpResponse('This is the index view for app1')
