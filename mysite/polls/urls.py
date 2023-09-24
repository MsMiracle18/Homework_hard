from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # URL-шляхи для вашого додатку
    path('', views.index, name='index'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quotes/', views.quote_list, name='quote_list'),
    path('quotes/<int:quote_id>/', views.quote_detail, name='quote_detail'),
    path('tags/', views.tag_list, name='tag_list'),
    path('tags/<int:tag_id>/', views.tag_detail, name='tag_detail'),
]
