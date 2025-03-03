from django import forms
from .models import Contato, Artigo


class ContatoForm(forms.ModelForm):

    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'mensagem']


class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ['titulo', 'resumo', 'conteudo', 'imagem']
