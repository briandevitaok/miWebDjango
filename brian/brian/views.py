from django.http import HttpResponse
from django.shortcuts  import  render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import  redirect
from django.contrib import  messages
from .forms import  RegistroForm, FormContact
from django.contrib.auth.models import User
from posteos.models import Posteos


def index(request):

    return render(request, 'index.html', {
    })

def login_view(request):
    if request.user.is_authenticated:
        messages.error(request, 'Usted se encuentra autenticado')
        return redirect ('index')
    if request.method == 'POST':
        username = request.POST.get('username') #Esto es un diccionario
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)#Si el usuario existe devuelve un user sino None
        if  user:
            login(request, user)
            messages.success(request, f'Bienvenido {username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o password no valido')
    return render(request, 'users/login.html', {
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect ('login')

def registro(request):
    if request.user.is_authenticated:
        messages.error(request, 'Usted se encuentra registrado')
        return redirect ('index')
    form = RegistroForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Registro exitoso')
            return redirect ('index')


    return render(request, 'users/registro.html', {
    'form': form,
    })


def contacto(request):
    form = FormContact(request.POST or None)

    return render(request, 'contacto.html',{
    'form':form
    })


def post(request):
    posteos = Posteos.objects.all()
    return render(request, 'posteos.html',{
    'posteos': posteos,
    })
