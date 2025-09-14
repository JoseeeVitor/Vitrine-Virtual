from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome


class Loja(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE,related_name='loja')
    nome          = models.CharField(max_length=100)
    telefone       = models.CharField("Telefone para contato", max_length=20, blank=True)
    descricao     = models.TextField("Breve descrição")
    endereco      = models.CharField("Endereço", max_length=200)
    categoria     = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    imagem        = models.ImageField(upload_to='lojas/logos/', null=True, blank=True)
    cover_image   = models.ImageField(upload_to='lojas/covers/', null=True, blank=True)
    profile_image = models.ImageField(upload_to='lojas/avatars/', null=True, blank=True)
    telefone = models.CharField(max_length=20, blank=True,help_text="Número de telefone para contato")
    horario_funcionamento = models.CharField(max_length=100,blank=True,help_text="Ex: Seg–Sex 08:00–18:00; Sáb 08:00–12:00")
    def __str__(self):
        return self.nome


class Produto(models.Model):
    loja      = models.ForeignKey(Loja, related_name='produtos', on_delete=models.CASCADE)
    nome      = models.CharField(max_length=100)
    descricao = models.TextField()
    preco     = models.DecimalField(max_digits=10, decimal_places=2)
    imagem    = models.ImageField(upload_to='produtos/', null=True, blank=True)

    def __str__(self):
        return self.nome
