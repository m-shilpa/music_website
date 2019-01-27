from django.conf.urls import url
from . import views

# admin: username: admin , password: pass1234.

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$',views.index,name='index'),

    # /music/album_id/  eg. /music/21/
    url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'),


    # /music/album_id/favorite/    eg. /music/21/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite, name='favorite'),

]

