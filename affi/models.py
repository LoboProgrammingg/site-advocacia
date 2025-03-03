from django.db import models


class Advogado(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    formacao = models.TextField()
    experiencia = models.TextField()
    certificacoes = models.TextField()
    foto = models.ImageField(upload_to='advogado_foto/')

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50, choices=[
        ('consultoria', 'Consultoria Jurídica'),
        ('falencias', 'Falências e Recuperações Judiciais'),
        ('outros', 'Outros Serviços'),
    ])
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Advogado, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class PerguntaFAQ(models.Model):
    pergunta = models.CharField(max_length=255)
    resposta = models.TextField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.pergunta


class Requerimento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    tipo_servico = models.ForeignKey(Servico, on_delete=models.CASCADE, default=1)
    descricao = models.TextField()
    arquivo = models.FileField(upload_to='requerimentos/', null=True, blank=True)

    def __str__(self):
        return f"Requerimento de {self.nome_cliente}"


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=15, null=True, blank=True)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contato de {self.nome}'


class Testemunho(models.Model):
    cliente_nome = models.CharField(max_length=255)
    depoimento = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Testemunho de {self.cliente_nome}'


class Agendamento(models.Model):
    cliente_nome = models.CharField(max_length=255)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=15)
    data_agendada = models.DateTimeField()
    mensagem = models.TextField(null=True, blank=True)
    confirmado = models.BooleanField(default=False)

    def __str__(self):
        return f'Agendamento de {self.cliente_nome} para {self.data_agendada}'


class FalenciaRecuperacao(models.Model):
    empresa = models.CharField(max_length=255)
    pedido = models.DateField()
    tipo = models.CharField(max_length=50)
    documento = models.FileField(upload_to='documentos/', null=True, blank=True)
    acesso_documento = models.BooleanField(default=False)

    def __str__(self):
        return self.empresa
