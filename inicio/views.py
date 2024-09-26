from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Cliente  # Importe o modelo de usuário


def login_view(request):
    erro = None
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        try:
            # Consultar no banco se existe um usuário com esse CPF e senha
            usuario = Usuario.objects.get(cpf=cpf, senha=senha)
            # Se o usuário for encontrado, o login foi bem-sucedido
            return redirect('telaInicio')
        except Usuario.DoesNotExist:
            # Se não for encontrado, exibe mensagem de erro
            erro = "CPF ou senha inválidos."
            return HttpResponse(erro)

    # Renderizar o formulário de login novamente se não for POST ou se houver erro
    return render(request, 'login.html', {'erro': erro})


def tela_inicial(request):
    return render(request, 'tela_inicial.html')


def cadastrar_cliente(request):
    if request.method == 'POST':        
        
        nome = request.POST.get('nome').upper()
        telefone = request.POST.get('telefone')
        data_cadastro = request.POST.get('data_cadastro')


        # Inserir os dados no banco de dados
        cliente = Cliente(nome=nome, telefone=telefone, data_cadastro=data_cadastro)
        cliente.save()
        
        success_message = "Cliente cadastrado com sucesso!"

        # Redirecionar após o cadastro
        return render(request, 'tela_inicial.html', {'success_message': success_message})  # Redireciona para a tela inicial ou para onde quiser

    # Apenas para renderizar a página se o método for GET
    return render(request, 'cadastrar_cliente.html')
