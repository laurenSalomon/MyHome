from django.shortcuts import render,redirect
from django.http import HttpResponse as reponse
from .forms import InscriptionForm,AgenceProfilForm
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def inscription(request):
    inscrire = InscriptionForm()
    agence =AgenceProfilForm()
    if request.method=="POST":
        inscrire = InscriptionForm(request.POST)
        if inscrire.is_valid():
            user =inscrire.save()
            if user.role=="agence":
                profile_agence =AgenceProfilForm(request.POST)
                if profile_agence.is_valid():
                    ag=profile_agence.save(commit=False)
                    ag.utilisateur=user
                    ag.save()
        return redirect('oups')
    context ={'inscrire':inscrire,"agence":agence}
    return render(request,'Utilisateurs/inscription.html',context)


def connexion(request):
    if request.method=="POST":
        form = connexionForm(request.POST)
        username =request.POST['username']
        password =request.POST['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return reponse('Bonjour')
        else:
            return reponse('Bye')
    else: 
        form = connexionForm()

    context ={
        'form':form
    }
    return render(request,'Utilisateurs/login.html',context)

def profile (request):
    profilAgence =AgenceProfilForm(instance =request.user.agenceprofil)
    modifierProfil=AgenceProfilUpdateForm(instance =request.user.agenceprofil)
    profilStandard =ProfilForm(instance =request.user.profile)
    if request.method=="POST":
        modifierProfil=AgenceProfilUpdateForm(request.POST,instance =request.user.agenceprofil)
        profilStandard =ProfilForm(request.POST,instance =request.user.profile)
        if profilStandard.is_valid() or modifierProfil.is_valid() :
            profilStandard.save()
            modifierProfil.save()
            return redirect('profil')
        
    

    context={
        'agence':profilAgence,
        'is_agence':request.user.role == "agence",
        'update':modifierProfil,
        'prost':profilStandard
    }
    return render(request,"Utilisateurs/profile.html",context)



