from django.shortcuts import render,HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def home (request):
    return render (request , 'comptes/login.html')


def register (request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        mon_utilisateur = User.objects.create_user(username,firstname,password)
        mon_utilisateur.first_name = firstname
        mon_utilisateur.save()
        messages.success(request,'votre compte a ete creer avec success')
        return redirect('login')

    return render(request , 'comptes/register.html')
def logIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            firstname = user.first_name
            messages.success(request, f"Bienvenue, {firstname} !")
            return redirect('home')  # Assurez-vous que cette URL est définie
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('login')

    return render(request, 'comptes/login.html')

def logOut (request): 
   logout(request)
   messages.success(request,'vous avez ete bien deconnecter')
   return redirect('homme')