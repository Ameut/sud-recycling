from django import forms
from .models import PageIndex, PageEconomieCirculaire, Matiere, DemandeDevis, Temoin, Inventaire, Image, Localisation, InformationAgence, Contact, Balle

class PageIndexForm(forms.ModelForm):
    class Meta:
        model = PageIndex
        fields = ['titre', 'description', 'image']

class PageEconomieCirculaireForm(forms.ModelForm):
    class Meta:
        model = PageEconomieCirculaire
        fields = ['titre', 'description', 'image']

class MatiereForm(forms.ModelForm):
    class Meta:
        model = Matiere
        fields = ['nom', 'coefficient']

class DemandeDevisForm(forms.ModelForm):
    class Meta:
        model = DemandeDevis
        fields = ['nom', 'email', 'telephone', 'message', 'matieres']

class TemoinForm(forms.ModelForm):
    class Meta:
        model = Temoin
        fields = ['nom', 'note', 'commentaire']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['titre', 'fichier_image', 'page']

class LocalisationForm(forms.ModelForm):
    class Meta:
        model = Localisation
        fields = ['ville', 'adresse']

class InformationAgenceForm(forms.ModelForm):
    class Meta:
        model = InformationAgence
        fields = ['localisation', 'numero_telephone', 'email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'email', 'commentaires']

class InventaireForm(forms.ModelForm):
    class Meta:
        model = Inventaire
        fields = ['matiere', 'volume_m3']

class BalleForm(forms.ModelForm):
    class Meta:
        model = Balle
        fields = ['nom', 'nombre', 'inventaire']
        
class DemandeDevisForm(forms.ModelForm):
    class Meta:
        model = DemandeDevis
        fields = ['nom', 'email', 'telephone', 'message', 'matieres', 'localisation']

    localisation = forms.ModelChoiceField(queryset=Localisation.objects.all(), empty_label="Sélectionnez une localisation")