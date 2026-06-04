from django.shortcuts import render,redirect,get_object_or_404
from google import genai
from django.http import HttpResponse
from .models import User_Info
from .gemini import health_remarks
from .forms import Blood_Sample
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.GET.get('next'): #To ensure login required page is redirected to login page with msg
        messages.info(request, "You need to login first to continue.")        
    form=AuthenticationForm(request,data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user=form.get_user()
            login(request, user) #Authenticates user by checking into database 
            return redirect("MIRA:health_predict")
    return render(request, "MIRA/login.html", {"form": form}) #designated template 

def sign_up(request):
    form=UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user=form.save() #saves new user data into database
        login(request, user)
        return redirect("MIRA:health_predict")
    return render(request, "MIRA/sign_up.html", {"form": form})

#form is first falsely saved in an object to retrieve user this helps in retriving records in records view as my form does not have user field.

@login_required   
def health_predict(request):
    #to temporary test api working : print(settings.GEMINI_API_KEY)
    form = Blood_Sample(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        health_details = form.save(commit=False) 
        health_details.user=request.user
        health_details.save()
        remarks = health_remarks(health_details)
        health_details.remarks= remarks
        health_details.save()
        return render(request , "MIRA/remarks.html",{"remarks": remarks})
    return render(request, "MIRA/home.html", {"form": form})

@login_required
def records(request):
    records = User_Info.objects.filter(user=request.user).order_by("-record_date")
    return render(request,"MIRA/records.html",{"records":records})

def edit_view(request,pk):
    record = get_object_or_404(User_Info,pk=pk)#user can only see her own records and pk is for specific entry
    form = Blood_Sample(request.POST or None, instance=record)#shows pre filled data
    if request.method == 'POST' and form.is_valid():#allows changes and redirects to api for new remarks
        health_details=form.save()
        remarks = health_remarks(health_details)
        health_details.remarks= remarks
        health_details.save()
        return redirect("MIRA:records")
    return render(request, "MIRA/home.html", {"form": form})

def delete_view(request,pk):
    record = get_object_or_404(User_Info,pk=pk)
    record.delete()
    return redirect("MIRA:records")

    

    
    