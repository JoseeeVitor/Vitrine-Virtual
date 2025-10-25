from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Categoria(models.Model):  ###Definição das categorias de lojas
    nome = models.CharField(max_length=100)  ###Nome da categoria
    slug = models.SlugField(unique=True)     ###Identificador único para um URL melhor
    def __str__(self):    
        return self.nome  ###Retorna o nome da categoria como representação

class Loja(models.Model):  ###Tudo que uma loja tem que ter
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='loja')
    nome = models.CharField(max_length=100)
    telefone = models.CharField("Telefone para contato", max_length=20, blank=True)
    descricao = models.TextField("Breve descrição")
    endereco = models.CharField("Endereço", max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    cover_image = CloudinaryField('image',null=True, blank=True,transformation={'format': 'jpg', 'quality': 'auto'})
    profile_image = CloudinaryField('image',null=True, blank=True,transformation={'format': 'jpg', 'quality': 'auto'}) 
    horario_funcionamento = models.CharField(max_length=100, blank=True, help_text="Ex: Seg-Sex 08:00-18:00; Sab 08:00-12:00")
    def __str__(self):
        return self.nome  ###Retorna o nome da loja como representação

class Produto(models.Model): ###Tudo que um produto tem que ter
    loja = models.ForeignKey(Loja, related_name='produtos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = CloudinaryField('image',null=True, blank=True,transformation={'format': 'jpg', 'quality': 'auto'})
    def __str__(self):
        return self.nome  ###Retorna o nome do produto como representação
