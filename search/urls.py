from django.conf.urls import url
from django.contrib import admin
from .views import (searchposts)

urlpatterns = [
     url(r'^$', searchposts, name='search course or professor'),

]
