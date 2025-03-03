from django.contrib import admin
from .models import Advogado, Servico, Artigo, PerguntaFAQ, Requerimento, Contato, Testemunho, Agendamento, FalenciaRecuperacao

admin.site.register(Advogado)
admin.site.register(Servico)
admin.site.register(Artigo)
admin.site.register(PerguntaFAQ)
admin.site.register(Requerimento)
admin.site.register(Contato)
admin.site.register(Testemunho)
admin.site.register(Agendamento)
admin.site.register(FalenciaRecuperacao)
