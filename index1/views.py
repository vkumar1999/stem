# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import Post



def home(request):
    
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')


def blog(request):
    posts = Post.objects.all()
    context={
    'Post' :  posts,
    }
    return render(request,'blog.html',context)

    # class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    # template_name = 'blog.html'


def contact(request):
    return render(request,'contact.html')



