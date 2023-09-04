from django.urls import path
from . import views
urlpatterns = [
     path('',views.profile, name='profile'),
     path('addpost/',views.addpost, name='addpost'),
     path('categories/<int:category_id>/', views.category_posts, name='category_posts'),
     #  path('create/', views.create_post, name='create_post'),
     path('postlist/', views.post_list, name='post_list'),

    
]