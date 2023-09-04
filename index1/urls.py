from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    # path('', views.homer, name='home'),
    path("myapp/",include('myapp.urls')),
    path('about/', views.about, name='about'),
    path('contact/',include('contact.urls')),
    path('blog/', views.blog, name='blog'),
    path("profilee/",include('profilee.urls')),
    path("categories/",include('categories.urls')),
    
    
    
]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)