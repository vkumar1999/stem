from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Category

# Create your views here.
@login_required(login_url='login')
def profile(request):
    #return HttpResponse('this is a homepage')
    return render(request, 'profile.html')
# def addpost(request):
#     #return HttpResponse('this is a homepage')
#     return render(request, 'addpost.html')
def addpost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')
        category = Category.objects.get(pk=category_id)
        new_post = BlogPost(title=title, content=content, image=image, category=category)
        # Save the blog post to the database
        new_post.save()
        return redirect('post_list')  # Redirect to the post_list view
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'addpost.html', context)
def post_list(request):
    posts = BlogPost.objects.all()
    context = {'posts': posts}
    return render(request, 'post_list.html', context)
def category_posts(request, category_id):
    category = Category.objects.get(pk=category_id)
    posts = BlogPost.objects.filter(category=category)
    context = {'category': category, 'posts': posts}
    return render(request, 'category_posts.html', context)











