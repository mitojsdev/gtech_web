from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Cliente  # Importe o modelo de usuário
from django.contrib import messages


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

        try:

            # Inserir os dados no banco de dados
            cliente = Cliente(nome=nome, telefone=telefone, data_cadastro=data_cadastro)
            cliente.save()

            messages.success(request, 'Cliente cadastrado com sucesso!')
        except Exception as e:
            if 'unicidade' in str(e):
                messages.error(request,'Ocorreu um erro ao inserir o cliente. Cliente informado já existe.')
            else:
                messages.error(request,'Ocorreu um erro ao inserir o cliente. Tente novamente.')
            
        return redirect('telaInicio')
    # Apenas para renderizar a página se o método for GET
    return render(request, 'cadastrar_cliente.html')

def pesquisar_cliente(request):
    nome = request.GET.get('nome', '')
    telefone = request.GET.get('telefone', '')
    
    # Consulta de clientes com base no nome e telefone (caso fornecidos)
    clientes = Cliente.objects.all()
    
    if nome:
        clientes = clientes.filter(nome__icontains=nome)
    if telefone:
        clientes = clientes.filter(telefone__icontains=telefone)
    
    context = {
        'clientes': clientes,
        'nome': nome,
        'telefone': telefone
    }
    
    return render(request, 'pesquisar_cliente.html', context)
