from django.shortcuts import get_object_or_404, render
from django import forms
from django.urls import reverse_lazy
from .models import pacientesAtivo,pesquisasAtiva
from usuarios.models import Profissional, Paciente
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView


# Create your views here.
def handleForms(post):
     List = {}
     for a in post:
          if a != 'csrfmiddlewaretoken':
               List[a] = post.get(a)
               # print(a)
     return List

#NavBar
@login_required
def Base(request):
     return render (request,"base.html")

#footer
@login_required
def Footer(request):
     return render (request,"Footer.html")


def cadastroPesquisa(request):
    if request.method=='POST':
          form = handleForms(request.POST)
          form["Profissional"] = Profissional.objects.get(id=form['Profissional'])
          print(form)
          pesquisasAtiva.objects.create(**form)
    return render (request,"Interface/cadastroPesquisa.html",{"form":CadastroForm()})

def formulario(request):
    if request.method=='POST':
          form = handleForms(request.POST)
          print(form)
          pesquisasAtiva.objects.create(**form)
    return render (request,"Interface/formulario.html",{"form":CadastroForm()})
    
def home(request):
    if request.method=='POST':
          form = handleForms(request.POST)
          print(form)
          pesquisasAtiva.objects.create(**form)

    return render(request,'Interface/home.html')

# class perfilUpdate(UpdateView):
#     template_name="cadastros/form.html"
#     model= Perfil
#     fields = ["nome", "cpf", "e-mail"]
#     success_url = reverse_lazy('index')

#     def get_object(self, queryset: None):
#         self.object = get_object_or_404(Perfil, usuario=self.request.user)
#         return self.object

#     def






class CadastroForm (forms.ModelForm):
    class Meta:
        model= pesquisasAtiva
        fields = ('CAAE', "Profissional", "TCLE","TImagemVoz")


