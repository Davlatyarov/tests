from django.shortcuts import render,redirect
from .forms import *
from django.views import View
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.http import HttpResponseRedirect

class RegisterView(View):

    def get(self,request):
        form = RegisterForm()
        
        return render(request, 'users/register.html', context={'form':form})

    
    def post(self,request):
        
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
        
        return HttpResponseRedirect(reverse('users:login'))
        return render(request, 'users/register.html', {'form': form})
    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', context={'form': form})

    def post(self, request):
        form2 = LoginForm(request.POST)
        if form2.is_valid():
            clean_data = form2.cleaned_data

            user = authenticate(username=clean_data['username'],password=clean_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index') 
            else:
                form2.add_error(None, 'Invalid username or password')
        return render(request, 'users/login.html',context={'form': form2})


