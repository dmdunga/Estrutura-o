from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User


# Create your views here.
def singin(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        seo_specialist = authenticate(username=username, password=password)
        login(request, seo_specialist)
        return redirect("logado")
    return render(request, 'authenticate/singin.html', {})


@login_required
def logado(request):
    # logout(request)
    return render(request, 'authenticate/logado.html', {})


def Cadastro(request):
    if request.method == 'POST':
        print(request.POST)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        CPF = request.POST.get('CPF')
        cnpj = request.POST.get('cnpj')
        Phone = request.POST.get('Phone')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        estado = request.POST.get('estado')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, CPF=CPF, Phone=Phone, username=username,
                                   password=password, cep=cep, cnpj=cnpj, rua=rua, bairro=bairro, cidade=cidade, estado=estado, numero=numero, complemento=complemento)
        user.set_password(password)
        user.save()
        return redirect('../infomacaoEmail', {})
        # return HttpResponse("Por favor, acessar o seu e-mail para confirmação do cadastro")

    data = {}
    data['Cadastro'] = UserForms()

    return render(request, 'authentication/singin.html', data)
