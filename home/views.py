from django.shortcuts import render


# Create your views here.

def index(request):
    print('HOME')
    return render(
        request,
        'home/index.html'
    )