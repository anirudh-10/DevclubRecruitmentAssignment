from django.urls import path
from .views import (
    PostListView,
    )
from . import views
from .models import courses

urlpatterns = [
    path('courses/', PostListView.as_view(model=courses), name='courses')
    ,
    
]
