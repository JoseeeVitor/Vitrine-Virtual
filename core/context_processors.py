from .models import Loja

def loja_do_usuario(request):
    loja = None
    if request.user.is_authenticated:
        try:
            loja = Loja.objects.get(usuario=request.user)
        except Loja.DoesNotExist:
            pass
    return {'user_loja': loja}