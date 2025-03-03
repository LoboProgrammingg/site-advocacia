from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import ContatoForm
from .models import Advogado, Servico, Artigo, PerguntaFAQ, Requerimento, Testemunho, Agendamento, FalenciaRecuperacao


def home(request):
    advogado = Advogado.objects.first()
    servicos = Servico.objects.filter(ativo=True)
    artigos = Artigo.objects.filter(ativo=True).order_by('-data_publicacao')[:3]
    falencias = FalenciaRecuperacao.objects.all()
    perguntas = PerguntaFAQ.objects.filter(ativo=True)

    return render(request, 'home.html', {
        'advogado': advogado,
        'servicos': servicos,
        'artigos': artigos,
        'falencias': falencias,
        'perguntas': perguntas,
    })


def sobre(request):
    advogado = Advogado.objects.first()
    return render(request, 'sobre.html', {'advogado': advogado})


def servicos_list(request):
    servicos = Servico.objects.filter(ativo=True)
    paginator = Paginator(servicos, 6)
    page = request.GET.get('page')
    servicos_paginados = paginator.get_page(page)

    return render(request, 'servicos_list.html', {'servicos': servicos_paginados})


def servico_detail(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    return render(request, 'servico_detail.html', {'servico': servico})


def artigos_list(request):
    artigos = Artigo.objects.filter(ativo=True).order_by('-data_publicacao')
    
    # Configurando a paginação
    paginator = Paginator(artigos, 6)  # 6 artigos por página
    page = request.GET.get('page')
    artigos_paginados = paginator.get_page(page)
    
    return render(request, 'artigos_list.html', {'artigos': artigos_paginados})


def artigo_detail(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'artigo_detail.html', {'artigo': artigo})


def faq(request):
    perguntas = PerguntaFAQ.objects.filter(ativo=True)
    return render(request, 'faq.html', {'perguntas': perguntas})


def requerimento(request):
    if request.method == 'POST':
        nome_cliente = request.POST['nome_cliente']
        email_cliente = request.POST['email_cliente']
        tipo_servico = Servico.objects.get(id=request.POST['tipo_servico'])
        descricao = request.POST['descricao']

        arquivo = request.FILES.get('arquivo', None)

        requerimento = Requerimento(
            nome_cliente=nome_cliente,
            email_cliente=email_cliente,
            tipo_servico=tipo_servico,
            descricao=descricao,
            arquivo=arquivo
        )
        requerimento.save()

        return render(request, 'requerimento_sucesso.html')

    servicos = Servico.objects.filter(ativo=True)
    return render(request, 'requerimento.html', {'servicos': servicos})


def contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua mensagem foi enviada com sucesso!')
            return redirect('home')
    else:
        form = ContatoForm()

    return render(request, 'home.html', {'form': form})


def testemunhos(request):
    testemunhos = Testemunho.objects.all()
    return render(request, 'testemunhos.html', {'testemunhos': testemunhos})


def agendamento(request):
    if request.method == 'POST':
        nome_cliente = request.POST['nome_cliente']
        email_cliente = request.POST['email_cliente']
        telefone_cliente = request.POST['telefone_cliente']
        data_agendada = request.POST['data_agendada']
        mensagem = request.POST.get('mensagem', '')

        agendamento = Agendamento(
            cliente_nome=nome_cliente,
            email_cliente=email_cliente,
            telefone_cliente=telefone_cliente,
            data_agendada=data_agendada,
            mensagem=mensagem
        )
        agendamento.save()
        return render(request, 'agendamento_sucesso.html')

    return render(request, 'agendamento.html')
