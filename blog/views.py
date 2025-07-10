from django.shortcuts import render
from blog.data import posts
from django.http import Http404
from typing import Any
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


def post(request, post_id):

    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')
    
    context =  {
            'post': found_post,
            'title': found_post['title'] + ' - '
    }

    return render(
        request,
        'blog/post.html',
        context
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

