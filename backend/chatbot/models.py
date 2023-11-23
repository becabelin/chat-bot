from django.db import models

class Resposta(models.Model):
    codigo = models.IntegerField()
    valor = models.CharField(max_length=1)
    descricao = models.TextField(blank=False, null=False)
    acao = models.TextField(blank=False, null=False)

class Pergunta(models.Model):
    codigo = models.IntegerField()
    titulo = models.TextField(blank=False, null=False)
    respostas = models.ManyToManyField(Resposta)