from django.shortcuts import render, get_object_or_404, redirect    # Importa funções essenciais do Django e outros arquivos do projeto
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Loja, Categoria, Produto
from .forms import LojaForm
from .forms import ProdutoForm

def home(request):                                                  # Página inicial com lista de lojas
    q = request.GET.get('q','')                                     # Parâmetro de busca na barra de pesquisa
    cat_slug = request.GET.get('categoria', '')                     # Parâmetro do filtro por categoria
    lojas = Loja.objects.all()
    if q:
        lojas = lojas.filter(nome__icontains=q)                     # Filtra pela busca
    if cat_slug:                                                    #Filtra pela categoria
        lojas = lojas.filter(categoria__slug=cat_slug)

    lojas_para_carrossel = Loja.objects.all()                       # Carrossel de lojas na home independente dos filtros
    categorias = Categoria.objects.all()

    context = {
    'lojas': lojas,                                                 # A lista completa de lojas (filtrada ou não).
    'lojas_para_carrossel': lojas_para_carrossel,                   # A lista SÓ para o carrossel.
    'busca': q,                                                     # O termo buscado (se houver).
    'categorias': categorias,                                       # A lista de categorias para o filtro.
    'selecionadas': cat_slug,                                       # A categoria selecionada (se houver).
    }
    return render(request, 'home.html', context)                    # Renderiza a página inicial com o contexto

def loja_view(request, loja_id):                                    # Exibição de uma loja específicada pelo id
    loja = get_object_or_404(Loja, id=loja_id)                       #se não encontrar a loja retorna 404 erro
    return render(request,'loja.html',{'loja': loja})                # Renderiza a página da loja

def signup_view(request):                                           # Cadastro de novos usuários
    form = UserCreationForm(request.POST or None)                   # Usa um formulário padrão de criação de usuário do Django
    if request.method=='POST' and form.is_valid():                  # Verifica se o formulário foi enviado e é válido
        user = form.save()                                          # Salva o novo usuário
        auth_login(request,user)                                    # Realiza o login automático do novo usuário
        return redirect('criar_loja')                               # Redireciona para a página de criação de loja
    return render(request,'signup.html',{'form':form})              # Renderiza a página de cadastro com o formulário

def login_view(request):                                            # Login de usuários
    form = AuthenticationForm(request, data=request.POST or None)   # Formulário de autenticação
    if request.method == 'POST' and form.is_valid():                # Verifica se o formulário foi enviado e é válido
        user = form.get_user()                                      # Obtém o usuário autenticado      
        auth_login(request, user)                                   # Realiza o login do usuário
        
        try:                                                        
            loja = Loja.objects.get(usuario=user)                   # Obtém a loja do usuário
            return redirect('loja',   loja_id=loja.id)              # Redireciona o usuario para a pagina dele
        except Loja.DoesNotExist:                                   # Se não encontrar a loja 
            return redirect('criar_loja')                           # Redireciona para a página de criação de loja       
        
    return render(request, 'login.html', {'form': form})            # Renderiza a página de login com o formulário novamente

def logout_view(request):                                           # Logout do usuário
    auth_logout(request)
    return redirect('home')                                         # Após o logout redireciona para a página inicial 

@login_required                                                     # verifica se o usuário está logado
def criar_loja(request):                                            # Criação de nova loja
    if request.method == 'POST':                                    # Só inicia o processo se o user enviar o formulário
        form = LojaForm(request.POST, request.FILES)                # Processa o formulário de criação de loja
        if form.is_valid():                                         
            loja = form.save(commit=False)                          # Cria a instância da loja sem salvar ainda
            loja.usuario = request.user                             # Atribui o usuário logado como dono da loja
            loja.save()
            return redirect('loja', loja_id=loja.id)                # Redireciona para a página da nova loja
        
    else:                                                           # Se o método não for POST, cria um formulário vazio
        form = LojaForm()           
    return render(request, 'criar_loja.html', {'form': form})       # Renderiza a página de criação de loja com o formulário

@login_required                                                      
def editar_loja(request, loja_id):                                  # Edição de uma loja específica
    loja = get_object_or_404(Loja, id=loja_id, usuario=request.user) # Garante que só o dono da loja acesse
    if request.method=='POST':                                       #Só inicia o processo se o user enviar o formulário
        if 'remove_cover' in request.POST:                           # Verifica se o botão de remover capa foi clicado
            loja.cover_image.delete(save=True)                       # Deleta a imagem de capa em seguida salva a instância da loja
            return redirect('editar_loja', loja_id)                  # Redireciona para a mesma página de edição
        if 'remove_avatar' in request.POST:                          # Verifica se o botão de remover avatar foi clicado         
            loja.profile_image.delete(save=True)                     # Deleta a imagem de avatar e salva            
            return redirect('editar_loja', loja_id)                  
        form = LojaForm(request.POST, request.FILES, instance=loja)  #Processa o formulário de edição
        if form.is_valid():                                          
            form.save()
            return redirect('loja', loja_id)                 
    else:
        form = LojaForm(instance=loja)                                    # Pré-preenche o formulário com os dados atuais da loja
    return render(request,'editar_loja.html',{'form': form,'loja': loja}) # Renderiza a página de edição da loja com o formulário

@login_required
def criar_produto(request, loja_id):                                # Criação de novo produto na loja
    loja = get_object_or_404(Loja, id=loja_id, usuario=request.user) # Garante que só o dono da loja acesse

    if request.method == 'POST':                                     # Só inicia o processo se o user enviar o formulário
        form = ProdutoForm(request.POST, request.FILES)              # Processa o formulário de criação de produto
        if form.is_valid():
            produto = form.save(commit=False) 
            produto.loja = loja                                      # Atribui a loja ao produto
            produto.save()                                           # Salva o novo produto
            return redirect('loja', loja_id=loja.id)                 # Redireciona para a página da loja
    else:
        form = ProdutoForm()                                         # Se o método não for POST, cria um formulário vazio
    return render(request, 'produto_form.html', {'form': form,'loja': loja})

@login_required
def editar_produto(request, loja_id, produto_id):                   # Edição de um produto específico na loja
    loja = get_object_or_404(Loja, id=loja_id, usuario=request.user) # Garante que só o dono da loja acesse
    produto = get_object_or_404(Produto, id=produto_id, loja=loja)   # Garante que o produto pertença à loja do usuário

    if request.method == 'POST':                                    # Só inicia o processo se o user enviar o formulário
        form = ProdutoForm(request.POST, request.FILES, instance=produto) 
        if form.is_valid():
            form.save()
            return redirect('loja', loja_id=loja.id)                 # Redireciona para a página da loja
    else:
        form = ProdutoForm(instance=produto)                         # Pré-preenche o formulário com os dados atuais do produto

    return render(request, 'produto_form.html', {'form': form,
'loja': loja,'produto': produto,})                                   # Renderiza a página de edição do produto com o formulário