from django.shortcuts import render
from blog.data import posts
# Create your views here.

def blog(request):
    return render(
        request,
        'blog/index.html',
        {
            'texto': 'Olá Blog',
            'title': 'Essa é uma pagina de exemplo',
            'posts': posts
        }
    )


def exemplo(request):
    return render(
        request,
        'blog/exemplo.html',
        {
            'texto': 'Olá exemplo do Blog',
            'title': 'Essa é uma pagina de exemplo'

        }
    )