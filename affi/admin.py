from django.contrib import admin
from .models import Advogado, Servico, Artigo, PerguntaFAQ, Requerimento, Contato, Testemunho, Agendamento, FalenciaRecuperacao


@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_publicacao', 'ativo', 'imagem')
    search_fields = ('titulo', 'resumo', 'autor__nome')
    list_filter = ('ativo', 'data_publicacao', 'autor')
    fieldsets = (
        (None, {
            'fields': ('titulo', 'resumo', 'conteudo', 'autor', 'imagem', 'ativo')
        }),
    )
    ordering = ('-data_publicacao',)

admin.site.register(Advogado)
admin.site.register(Servico)
admin.site.register(PerguntaFAQ)
admin.site.register(Requerimento)
admin.site.register(Contato)
admin.site.register(Testemunho)
admin.site.register(Agendamento)
admin.site.register(FalenciaRecuperacao)
