from django.shortcuts import render,redirect
from .forms import uploadForm
from .models import uploadImg
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    fm=uploadForm()
    imgdb=None
    if request.user.is_authenticated:
        imgdb=uploadImg.objects.filter(author=request.user)
    if request.method == "POST":
        fm = uploadForm(request.POST, request.FILES)   
        if fm.is_valid():
            fm.save()
            messages.success(request,"Image uploaded!") 
            return redirect("home")
        else:
            messages.warning(request,"Image not uploaded!") 
    context={
        'form':fm,
        'imgdb':imgdb,
    }
    return render(request,"index.html",context)

def recent(request):
    imgdb=None
    if request.user.is_authenticated:
        imgdb=uploadImg.objects.order_by("-created_img").filter(author=request.user)
        context={
        'imgdb':imgdb,
    }
    return render(request,"index.html",context)

def previous(request):
    imgdb=None
    if request.user.is_authenticated:
        imgdb=uploadImg.objects.order_by("created_img").filter(author=request.user)
        context={
        'imgdb':imgdb,
    }
    return render(request,"index.html",context)

##delete img
def delImg(request,pk):
    if request.user.is_authenticated:
        member = uploadImg.objects.get(id=pk)
        member.delete()
        messages.success(request, "Image has deleted!!")
        return redirect("home")
    else:
        return redirect("login")