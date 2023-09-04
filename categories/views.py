from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
def categories(request):
    return HttpResponse("This is categories page")
    #return render(request,'categories/categories.html')
def science(request):
    #return HttpResponse("This is a science page")
    return render(request,'categories/science.html')
def technology(request):
    return render(request,'categories/technology.html')
def education(request):
    return render(request,'categories/education.html')
def medicine(request):
    return render(request,'categories/medicine.html')