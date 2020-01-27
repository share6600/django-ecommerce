from django.contrib.auth import authenticate , login,get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm , LoginForm , RegisterForm

def home_page(request):
  context={
    'title':'hello worlddd',
    'content':'content for home page',

    
  }
  if request.user.is_authenticated():
     context['premiumcontent']='yehhh'
  return render (request,'home_page.html',context)
def about_page(request):
  context={
    'title':'hello about',
    
  }  
  return render (request,'home_page.html',context)



def contact_page(request):
  contact_form=ContactForm(request.POST or None)
  context={
    'title':'hello contact',
    'content':'content for contact page',
    'form':contact_form
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  # if request.POST:
  #   print (request.POST.get('fullname'))
  #   print (request.POST.get('email'))
  #   print (request.POST.get('content'))
  return render (request,'contact/view.html',context)


def login_page(request):
  form=LoginForm(request.POST or None)
  context={
    'form':form
  }
  print("user log in")
  print(request.user.is_authenticated())

  if form.is_valid():
    print(form.cleaned_data)
    # context['form']=LoginForm()
    username=form.cleaned_data.get('username')
    password=form.cleaned_data.get('password')
    user = authenticate(request, username=username, password=password)
    print(request.user.is_authenticated())
    if user is not None:
        print(request.user.is_authenticated())
        login(request, user)
        # Redirect to a success page.
        return redirect('/')
    else:
        # Return an 'invalid login' error message.
        print('error')

  return render(request,"auth/login.html",context)
User=get_user_model()
def register_page(request):
  form=RegisterForm(request.POST or None)
  print(request.user.is_authenticated())
  context={
    'form':form
  }
  if form.is_valid():
    print(form.cleaned_data)
    username=form.cleaned_data.get('username')
    password=form.cleaned_data.get('password')
    email=form.cleaned_data.get('email')
    newuser=User.objects.creat_user(username,password,email)
    print(newuser)
  return render(request,"auth/register.html",context)