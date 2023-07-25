from django.db import models

class DadosEleitorais(models.Model):
    nome = models.CharField(max_length=100)
    titulo_eleitor = models.CharField(max_length=12)
    zona_eleitoral = models.IntegerField()
    secao_eleitoral = models.IntegerField()
    # Adicione outros campos conforme necessário
