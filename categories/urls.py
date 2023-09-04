from django.urls import path
from . import views
urlpatterns = [
    path('', views.categories, name='categories'),
    #path('home/', views.homer, name='homer'),
    path('1/', views.science, name='science'),
    path('2/', views.technology, name='technology'),
    path('3/', views.education, name='education'),
    path('4/', views.medicine, name='medicine'),
   
  #   path('', views.PostList.as_view(), name='categories'),
  # path('<slug:slug>/', views.PostList.as_view(), name='post_detail'),
]