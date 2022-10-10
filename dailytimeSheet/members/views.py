from genericpath import exists
from unicodedata import name
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
from datetime import  datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render

def index(request):
    #mymembers = Members.objects.all().values()
    
    template = loader.get_template('index.html')
    cuser=request.user
    print(cuser.username)
    if cuser.username == "admin":
        mymembers=Members.objects.all()
        context = {
        'mymembers': mymembers,
        'user':cuser,
        }
        return HttpResponse(template.render(context, request))
    elif Members.objects.filter(name = cuser.username).exists():
      mymembers=mymembers=Members.objects.filter(name = cuser.username)
      #mymembers=Members.objects.all()
      print("================")
      print(mymembers)
      context = {
      'mymembers': mymembers,
      'user':cuser,
       }
      return HttpResponse(template.render(context, request))
    else:
      return render(request,'login.html')


def add(request):
  template = loader.get_template('add.html')
  cuser=request.user
  context = {
    'user':cuser,
  }
  return HttpResponse(template.render(context, request))

def addrecord(request):
  n= request.POST['name']
  d=request.POST['dte']
  x = request.POST['vpne']
  y = request.POST['vpno']
  z= request.POST['officee']
  a= request.POST['officeo']

  vte=datetime.strptime(x,"%H:%M")
  vto=datetime.strptime(y,"%H:%M")
  ote=datetime.strptime(z,"%H:%M")
  oto=datetime.strptime(a,"%H:%M")

  vT=vto-vte
  oT=oto-ote
  T=vT+oT

  try:
    print(str(vT).split(",")[1])
    vT=str(vT).split(",")[1]
  except:
      print(str(vT).split(",")[0])
      vT=str(vT).split(",")[0].strip()

  try:
      print(str(oT).split(",")[1])
      oT=str(oT).split(",")[1].strip()
  except:
      print(str(oT).split(",")[0])
      oT=str(oT).split(",")[0].strip()  

  try:
      print(str(T).split(",")[1])
      T=str(T).split(",")[1].strip()
  except:
      print(str(T).split(",")[0])
      T=str(T).split(",")[0].strip() 

  member = Members(name=n, dte=d, ve=x, vo=y, oe=z, oo=a, vt=vT, ot=oT, tt=T)
  member.save()
  return HttpResponseRedirect(reverse('index'))


def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, id):
  member = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': member,
  }
  return HttpResponse(template.render(context, request))

def updaterec(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))

def signup(request):
    
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render(request,'signup.html',{'error':'Username is already taken!'}) 
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'signup.html',{'error':'password does note match!'})  
    else:
        return render(request,'signup.html')

def login(request):
    
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'login.html',{'error':'Username or password is incorrect!'})  #{'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return HttpResponseRedirect(reverse('login'))
