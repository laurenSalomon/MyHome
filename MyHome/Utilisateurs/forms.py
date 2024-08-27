from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser,AgenceProfil,Profile
from django.contrib.auth import get_user_model

User =get_user_model()
class InscriptionForm(UserCreationForm):
    password1 =forms.CharField(widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':'Votre mot de passe'
    }))
    password2 =forms.CharField(widget=forms.PasswordInput(attrs={
        'type':'password',
        'placeholder':' confirmer votre mot de passe'
    }))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'email','role','username' ,'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Masquer le texte d'aide pour les champs de mot de passe
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class connexionForm (AuthenticationForm):
    username =forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'votre mot de passe',
        'type':'text',
        'class':'input'
    }))
    password =forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'votre mot de passe',
        'type':'password',
        'class':'input'
    }))


class AgenceProfilForm(forms.ModelForm):
    class Meta:
        model =AgenceProfil
        fields =["nom_entreprise","Numero_enregistrement","statut_juridique"]

class AgenceProfilUpdateForm(forms.ModelForm):
    class Meta:
        model =AgenceProfil
        fields =["nom_entreprise","Numero_enregistrement","statut_juridique","annee_creation","slogan","adresse_siege_social","Site_web","profile_facebook","profile_instagram"]

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =["numero","creation_annee"]


    
