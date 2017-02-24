from django.shortcuts import render, redirect
from .models import User, Travel
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
        # insert travel informations to the context
    except User.DoesNotExist:
        messages.add_message(request, messages.INFO, msg)
        return redirect('/')
    return render(request,'login/travel.html',context)

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

def addtravel(request):
    if 'id'not in request.session:
        messages.error(request, 'Nice try, log in or register.')
        return redirect('/')
    print "successfully in addtravel route"
    return render(request, 'login/addplan.html')

def travel(request):
        if request.method != 'POST':
            return redirect('/')
        else:
            travel_valid = Travel.objects.addtravel(request.POST,request.session['id'])
            if travel_valid[0]==True:
                print "travel_valid", travel_valid
                return redirect('/success')
            else:
                print "flashes", travel_valid[1]
                for msg in travel_valid[1]:
                    messages.add_message(request,messages.INFO,msg)
                return redirect('/addtravel')
def back(request):
    if "id" not in request.session:
        return redirect('/')
    else:
        return redirect('/success')


def logout(request):
    if "id" in request.session:
        request.session.pop("id")
    return redirect('/')
