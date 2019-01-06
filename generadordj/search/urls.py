from django.conf.urls import url
from .views import searchlex


urlpatterns = [
    url(r'^search/$',searchlex, name = 'searchlex')
]