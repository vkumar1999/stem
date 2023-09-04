from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
     path('',views.authlogin, name='login'),
     path('register/',views.authregistration, name='register'),
    
    #  path('forgot-password/',views.forgotpassword, name='forgotpassword'),
     path('logout/',views.authlogout, name='logout'),
     path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='authentication/forgot.html'), name='forgotpassword'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentication/reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/reset_complete.html'), name='password_reset_complete'),
]






