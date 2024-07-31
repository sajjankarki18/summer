from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomCreationForm

# authentication routes

def loginUser(request):
    
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials! Please try again')
            return redirect('loginUser')
            
    return render(request, 'loginUser.html')

def registerUser(request):
    form = CustomCreationForm()
    
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            if password1 == password2:
                user = auth.authenticate(email=email, username=username, password = password1)
                
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    pass
            else:
                messages.info(request, 'Invalid password, please try again!')
                return redirect('registerUser')
    
    context = {'form': form}            
    return render(request, 'registerUser.html', context)

def logoutUser(request):
    logout(request)
    
    return redirect('loginUser')