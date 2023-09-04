from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def post_add(request):
    #return HttpResponse('this is a homepage')
    return render(request, 'postadd.html')