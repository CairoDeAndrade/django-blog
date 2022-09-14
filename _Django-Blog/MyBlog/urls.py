from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>', views.see_post, name='see_post'),
    path('bibliotecas/', views.see_library, name='see_library'),
    path('linguagem-python/', views.see_language, name='see_language'),
    path('noticias-python/', views.see_news, name='see_news'),
    path('search/', views.search, name='search'),
]
