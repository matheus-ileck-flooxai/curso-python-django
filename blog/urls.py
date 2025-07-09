from django.urls import path
from . import views

# MVT (MVC)


urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
 
]
