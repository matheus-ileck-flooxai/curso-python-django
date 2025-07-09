from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(
        request,
        'blog/index.html',
        {
            'texto': 'Olá Blog',
            'title': 'Essa é uma pagina de exemplo'
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