from django.shortcuts                       import render, get_object_or_404, redirect
from django.contrib.auth                    import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators         import login_required
from django.contrib.auth.forms              import AuthenticationForm, UserCreationForm
from .models                                import Loja, Categoria, Produto
from .forms                                 import LojaForm
from .forms                                 import ProdutoForm

def home(request):
    q    = request.GET.get('q','')
    cat_slug = request.GET.get('categoria', '')
    lojas = Loja.objects.all()
    if q:
        lojas = lojas.filter(nome__icontains=q)
    if cat_slug:
        lojas = lojas.filter(categoria__slug=cat_slug)

    lojas_para_carrossel = Loja.objects.all()       # Carrossel de lojas na home
    categorias = Categoria.objects.all()

    print("======================================")
    print(f"-> EXECUTANDO A VIEW 'HOME'")
    print(f"-> Lojas encontradas para o carrossel: {lojas_para_carrossel}")
    print(f"-> Número de lojas: {lojas_para_carrossel.count()}")
    print("======================================")

    context = {
    'lojas': lojas,                             # A lista principal, que pode ser filtrada.
    'lojas_para_carrossel': lojas_para_carrossel, # A lista SÓ para o carrossel.
    'busca': q,
    'categorias': categorias,
    'selecionadas': cat_slug,
    }

    return render(request, 'home.html', context)


def loja_view(request, loja_id):
    loja = get_object_or_404(Loja, id=loja_id)
    return render(request,'loja.html',{'loja': loja})


@login_required
def editar_loja(request, loja_id):
    loja = get_object_or_404(Loja, id=loja_id, usuario=request.user)
    if request.method=='POST':
        if 'remove_cover' in request.POST:
            loja.cover_image.delete(save=True)
            return redirect('editar_loja', loja_id)
        if 'remove_avatar' in request.POST:
            loja.profile_image.delete(save=True)
            return redirect('editar_loja', loja_id)
        form = LojaForm(request.POST, request.FILES, instance=loja)
        if form.is_valid():
            form.save()
            return redirect('loja', loja_id)
    else:
        form = LojaForm(instance=loja)
    return render(request,'editar_loja.html',{'form': form,'loja': loja})

#                                    LOGIN / LOGOUT / SIGNUP
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        auth_login(request, user)
        # busca a Loja diretamente pelo manager
        try:
            loja = Loja.objects.get(usuario=user)
            return redirect('loja',   loja_id=loja.id)
        except Loja.DoesNotExist:
            # se não tiver loja, redireciona para criar
            return redirect('criar_loja')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('home')

def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user = form.save()
        auth_login(request,user)
        return redirect('criar_loja')
    return render(request,'signup.html',{'form':form})

@login_required
def criar_loja(request):
    """
    Cria uma nova vitrine (Loja) para o usuário logado.
    URL: /criar-loja/
    """
    if request.method == 'POST':
        form = LojaForm(request.POST, request.FILES)
        if form.is_valid():
            loja = form.save(commit=False)
            loja.usuario = request.user
            loja.save()
            return redirect('loja', loja_id=loja.id)
    else:
        form = LojaForm()
    return render(request, 'criar_loja.html', {
        'form': form
    })

@login_required
def criar_produto(request, loja_id):
    # Garante que só o dono da loja acesse:
    loja = get_object_or_404(Loja, id=loja_id, usuario=request.user)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.loja = loja
            produto.save()
            return redirect('loja', loja_id=loja.id)
    else:
        form = ProdutoForm()

    return render(request, 'produto_form.html', {
        'form': form,
        'loja': loja
    })

@login_required
def editar_produto(request, loja_id, produto_id):
    loja = get_object_or_404(Loja, id=loja_id, usuario=request.user)
    produto = get_object_or_404(Produto, id=produto_id, loja=loja)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('loja', loja_id=loja.id)
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produto_form.html', {
        'form': form,
        'loja': loja,
        'produto': produto,
    })