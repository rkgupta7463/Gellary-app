from urllib import request
from django.shortcuts import redirect, render,HttpResponse
from django.http import HttpResponseServerError
# from signup.models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import socket

# @login_required(login_url="signin")
def signupUser(request):
        user = request.user
        if request.user.is_authenticated:
            return redirect("home")
        context = {}
        try:
            if request.method == 'POST':
                fname = request.POST.get('fname')
                lname = request.POST.get('lname')
                email = request.POST.get('email')
                username = request.POST.get('username')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')
                if User.objects.filter(username=username).first():
                    messages.error(
                        request, "This username is already taken! Please login with user id!")
                    return redirect('signup')
                if User.objects.filter(email=email).first():
                    messages.error(
                        request, "This email is already taken! Please login with user id")
                    return redirect('signup')

                if password1 == password2:
                    fname = request.POST.get("fname")
                    lname = request.POST.get("lname")
                    email = request.POST.get("email")
                    username = request.POST.get("username")
                    password1 = request.POST.get("password1")
                    password2 = request.POST.get("password2")

                    user = User.objects.create_user(
                        username=username, email=email, password=password1, first_name=fname, last_name=lname)
                    user.save()
                    # messages.success(request, "Welcome {}".format(request.user.get_short_name()))
                    # subject = "welcome to Rishu devloper & bloger"
                    # message = f"Hi {user.first_name}, Thank you for registering in Rishu devloper & bloger. Here You can gather the knowledge of basic blogs and programming knowledges. Like HTML, JS, CSS, PYTHON DJANGO, JAVA, WEB DEVELOPER, etc \n\n If you are get an any problems than contact on this email id :-\t rishukumargupta8409@gmail.com"
                    # email_from = settings.EMAIL_HOST_USER
                    # recipient_list = [user.email, ]
                    # send_mail(subject, message, email_from,
                    #         recipient_list, fail_silently=False)
                    return redirect("home")
                else:
                    messages.warning(request, 'Password must be same!')
                    return render(request, "auth/signup.html", context)
            else:
                return render(request, "auth/signup.html", context)
        except socket.gaierror:
            return HttpResponseServerError("Internet connection error")

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home")
    context = {}
    try:
        # if not socket.error:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request,"Welcome back {}".format(request.user.get_short_name()))
                return redirect("home")
            else:
                messages.warning(request, "User or password is not correct!")

        return render(request, "auth/login.html", context)

        # else:
    except socket.error:
        return HttpResponseServerError("Your Internet connection is very slow😒😒")

# def forget(request):
#     if request.POST == 'POST':
#         form = ForgetPass(user=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, "Password has changed Successfully!!")
#     else:
#         form = ForgetPass(user=request.user)

#     context = {'form': form}
#     return render(request, 'auth/forgetpass.html', context)

# logout function
@login_required(login_url="signin")
def logOutUser(request):
    try:
        logout(request)
        messages.success(request,"Logged Out successfully!")
        return redirect("home")
    except socket.gaierror:
        return HttpResponseServerError("Internet connection error")
