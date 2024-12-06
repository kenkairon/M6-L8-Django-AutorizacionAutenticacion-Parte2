from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')  # Redirigir al login después del registro
    else:
        formulario = UserRegistrationForm()
    return render(request, 'auth_app/register.html', {'form': formulario})


def index(request):
    return render(request, 'auth_app/index.html')

def home(request):
    return render(request, 'auth_app/home.html')