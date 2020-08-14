from django.shortcuts import render
from django import forms
# Create your views here.
class NewForm(forms.Form):
    base_digimon = forms.CharField(label="Base Digimon")
    end_digimon = forms.CharField(label="Base Digimon")

def search(request):

    form = NewForm()
    return render(request,"search/search.html",{"form":form})
