from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and len(password)>=8:
            login(request,user)
            messages.success(request, 'Login Successful')
            return redirect('profile')
        elif len(password)<8:
             messages.warning(request, 'Password should have atleast 8 characters')
        else:
            messages.warning(request, 'Username or Password Invalid!')
    return render(request,'authentication/login.html')
def authlogout(request):
    logout(request)
    messages.success(request, 'Logout Successfully !')
    return redirect('login')
def authregistration(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password and len(password)>=8:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username Already Exist')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email Already Exist')
            else:
                user = User.objects.create_user(username=username,password=password,email=email)
                user.save()
                messages.success(request, 'Account Successfully Created')
                return redirect('profile')
        elif password == confirm_password and len(password)<8:
            messages.warning(request, 'Password should have atleast 8 characters')
        else:
            messages.warning(request, 'Password and Confirm Password Not Matched')
    return render(request,'authentication/register.html')
# def forgotpassword(request):
#     return render(request,'authentication/forgot.html')
class CustomPasswordResetView(PasswordResetView):
    template_name = 'authentication/forgot.html'
    email_template_name = 'authentication/forgot.html'
    success_url = 'authentication/reset_done.html'