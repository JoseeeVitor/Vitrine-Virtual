from django.contrib import admin
from .models import Loja, Produto
from .models import Categoria

admin.site.register(Loja)
admin.site.register(Produto)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nome",)}
    list_display = ("nome", "slug")