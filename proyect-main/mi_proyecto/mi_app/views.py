from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a home después del login
        else:
            return render(request, 'mi_app/login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
    
    return render(request, 'mi_app/login.html')

def home(request):
    # Solo usuarios autenticados pueden ver home
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'mi_app/home.html')
