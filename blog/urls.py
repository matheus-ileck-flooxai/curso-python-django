from django.urls import path
from . import views

# MVT (MVC)


urlpatterns = [
    path('', views.blog, name='blog'),
    path('exemplo/', views.exemplo, name='exemplo'),
 
]
