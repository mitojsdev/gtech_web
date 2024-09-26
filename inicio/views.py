from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        # Capturando os dados do formulário
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        # Aqui você pode adicionar a lógica de verificação do CPF e senha
        # Por exemplo, vamos usar um exemplo simples para autenticar
        if cpf == "12345678900" and senha == "minha_senha":
            # Se as credenciais forem corretas, você pode redirecionar para outra página
            return HttpResponse(f"Bem-vindo, CPF {cpf}!")
        else:
            # Se o login falhar, você pode mostrar uma mensagem de erro
            return HttpResponse("CPF ou senha inválidos.")

    # Se for uma requisição GET, renderize o formulário
    return render(request, 'login.html')