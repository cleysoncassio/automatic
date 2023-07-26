# crm/dados_eleitorais/views.py
from django.shortcuts import render
from .models import DadosEleitorais
from django.http import HttpResponse


def home (request):
    context = {
        'title': 'Home',
    }
    return render(request, 'home.html', context)


def upload_csv(request):
    if request.method == 'POST' and request.FILES['arquivo']:
        arquivo = request.FILES['arquivo']
        # Processar o arquivo CSV e salvar os dados no banco de dados
        for linha in arquivo:
            dados = linha.decode('iso-8859-1').split(',')
            if len(dados) >= 4:
                nome = dados[0]
                titulo_eleitor = dados[1]
                zona_eleitoral = int(dados[2])
                secao_eleitoral = int(dados[3])
                # Criar um objeto DadosEleitorais com os dados do arquivo CSV
                DadosEleitorais.objects.create(
                    nome=nome,
                    titulo_eleitor=titulo_eleitor,
                    zona_eleitoral=zona_eleitoral,
                    secao_eleitoral=secao_eleitoral
                )
        return render(request, 'sucesso.html')
    else:
        return render(request, 'formulario_upload.html')
