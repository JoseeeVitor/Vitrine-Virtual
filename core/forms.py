from django import forms
from .models import Loja, Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'imagem']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows':3}),
        }


class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = [
            'nome',
            'telefone',
            'descricao',
            'imagem',        
            'endereco',
            'categoria',
            'cover_image',   
            'profile_image',
            'horario_funcionamento'
            
        ] 
        widgets = {'descricao': forms.Textarea(attrs={'rows':3}),  }        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cover_image'].required = False
        self.fields['profile_image'].required = False
        self.fields['imagem'].required = False
        self.fields['categoria'].required = False
