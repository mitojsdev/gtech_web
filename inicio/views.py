from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario  # Importe o modelo de usuário

def login_view(request):
    erro = None
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        try:
            # Consultar no banco se existe um usuário com esse CPF e senha
            usuario = Usuario.objects.get(cpf=cpf, senha=senha)
            # Se o usuário for encontrado, o login foi bem-sucedido
            return HttpResponse(f"Bem-vindo, CPF {cpf}!")
        except Usuario.DoesNotExist:
            # Se não for encontrado, exibe mensagem de erro
            erro = "CPF ou senha inválidos."
            return HttpResponse(erro)

    # Renderizar o formulário de login novamente se não for POST ou se houver erro
    return render(request, 'login.html', {'erro': erro})
