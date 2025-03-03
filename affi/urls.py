from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('servicos/', views.servicos_list, name='servicos_list'),
    path('servico/<int:servico_id>/', views.servico_detail, name='servico_detail'),
    path('artigos/', views.artigos_list, name='artigos_list'),
    path('artigo/<int:artigo_id>/', views.artigo_detail, name='artigo_detail'),
    path('faq/', views.faq, name='faq'),
    path('contato/', views.contato, name='contato'),
    path('requerimento/', views.requerimento, name='requerimento'),
    path('testemunhos/', views.testemunhos, name='testemunhos'),
    path('agendamento/', views.agendamento, name='agendamento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
