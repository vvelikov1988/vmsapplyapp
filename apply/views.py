from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
#from .models import User, Issue

def apply(request):
    return render(request, "apply.html")

def submitapply(request):
    errors = Applicant.objects.register_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/apply')
    else:
        a = Applicant.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            resume = request.POST['resume']
        )
        return redirect('/apply/success')

def successapply(request):
    return render(request, "success.html")