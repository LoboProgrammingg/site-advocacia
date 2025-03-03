# Generated by Django 5.1.6 on 2025-03-02 21:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advogado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('formacao', models.TextField()),
                ('experiencia', models.TextField()),
                ('certificacoes', models.TextField()),
                ('foto', models.ImageField(upload_to='advogado_foto/')),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nome', models.CharField(max_length=255)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('telefone_cliente', models.CharField(max_length=15)),
                ('data_agendada', models.DateTimeField()),
                ('mensagem', models.TextField(blank=True, null=True)),
                ('confirmado', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('mensagem', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerguntaFAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=255)),
                ('resposta', models.TextField()),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('consultoria', 'Consultoria Jurídica'), ('falencias', 'Falências e Recuperações Judiciais'), ('outros', 'Outros Serviços')], max_length=50)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testemunho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nome', models.CharField(max_length=255)),
                ('depoimento', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumo', models.TextField()),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affi.advogado')),
            ],
        ),
        migrations.CreateModel(
            name='Requerimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=255)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('descricao', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
                ('tipo_servico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='affi.servico')),
            ],
        ),
    ]
