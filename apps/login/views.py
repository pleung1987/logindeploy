from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    if "id" in request.session:
        return redirect('/success')
    return render (request,'login/index.html')

def success(request):
    if "id" not in request.session:
        return redirect('/')
    try:
        user= User.objects.get(id=request.session["id"])
        context={
            "user": user
        }
        print 80*"*"
        print "user", user
        print 80*"*"
    except User.DoesNotExist:
        messages.add_message(request, messages.INFO, msg)
        return redirect('/')
    return render(request,'login/success.html',context)

def process(request):
    if request.method != 'POST':
        return redirect('/')
    else:

        user_valid = User.objects.validation(request.POST)
        if user_valid[0]==True:
            request.session["id"]= user_valid[1].id
            return redirect('/success')
        else:
            print "flashes", user_valid[1]
            for msg in user_valid[1]:
                messages.add_message(request,messages.INFO,msg)
            return redirect('/')

def login(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        user_valid= User.objects.authenticate(request.POST)
        if user_valid[0]==True:
            request.session["id"]=user_valid[1].id
            # print 80*"*"
            # print "user_valid", user_valid
            # print 80*"*"
            return redirect('/success')
        else:
            # print 80*"*"
            # print "redirect to home"
            # print 80*"*"
            messages.add_message(request,messages.INFO,user_valid[1])
            return redirect('/')

def logout(request):
    if "id" in request.session:
        request.session.pop("id")
    return redirect('/')
