from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^playgame/', views.play_game, name = 'play_game'),
    url(r'^newgame/', views.new_game, name ='new_game'),
    url(r'^cachetest/', views.cache_test_page, name = 'cache_test_page'),
]
