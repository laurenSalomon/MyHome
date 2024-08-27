from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class CustomUser(AbstractUser):
    type =[
        ('client','Prospect Client'),
        ('agence','Agence immobilière'),
        ('proprietaire',"proprietaire de logement")
    ]
    role = models.CharField(max_length=100,choices=type,verbose_name='type d\'utilisateur')

User =get_user_model()
class Profile(models.Model):
    utilisateur =models.OneToOneField(User,on_delete=models.CASCADE)
    numero =models.IntegerField(verbose_name='Numero de telephone',blank=True,null=True)
    creation_annee = models.IntegerField(verbose_name='Année de création', default=datetime.datetime.now().year)
    
    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        print('Creation--',created)
        print('sender--',sender)
        print('instance--',instance)
        if created:
            Profile.objects.create(utilisateur=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender, instance,**kwargs):
        instance.profile.save()
        pass
    class Meta:
       db_table = 'Profil'
   


class AgenceProfil(models.Model):
    utilisateur =models.OneToOneField(User,on_delete=models.CASCADE)
    nom_entreprise =models.CharField(max_length=200,verbose_name='nom de l\'organisation')
    Numero_enregistrement=models.CharField(max_length=14,verbose_name='Numéro de registre de commerce')
    statut_juridique=models.CharField(max_length=20,verbose_name='SARL,SA',blank=True)
    annee_creation = models.DateField(verbose_name='Date de création', blank=True, null=True)
    slogan=models.CharField(max_length=200,verbose_name='Slogan de votre organisation',blank=True)
    adresse_siege_social =models.CharField(verbose_name='adresse physique',max_length=200,blank=True)
    Site_web=models.URLField(verbose_name='le site web de  l\'organisation',blank=True)
    profile_facebook =models.URLField(blank=True,null=True)
    profile_instagram =models.URLField(blank=True,null=True)
    profile_linked =models.URLField(blank=True,null=True)
    profile_twitter =models.URLField(blank=True,null=True)
    
    class Meta:
       db_table = 'AgenceProfile'

