from django.urls import path
from . import views
urlpatterns = [
     path('',views.post_add, name='post_add'),
     path('postadd/',views.post_add, name='post-add'),
]