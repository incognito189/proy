from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    """Vista para la página de inicio"""
    return render(request, 'mi_app/home.html')

def login_view(request):
    """Vista personalizada para el login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'mi_app/login.html')
    
    return render(request, 'mi_app/login.html')
