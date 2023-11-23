from ..models import Pergunta, Resposta


def obterHistorico():
    pergunta, created = Pergunta.objects.get_or_create(codigo=4)
    pergunta.titulo = 'Você tem histórico familiar de câncer?'

    resposta1, created = Resposta.objects.get_or_create(codigo=11)
    resposta1.valor = '1'
    resposta1.descricao = 'Sim'
    resposta1.acao = '/api/v1/chatbot/sintomasgerais'

    resposta2, created = Resposta.objects.get_or_create(codigo=12)
    resposta2.valor = '2'
    resposta2.descricao = 'Não'
    resposta2.acao = '/api/v1/chatbot/sintomasgerais'

    resposta3, created = Resposta.objects.get_or_create(codigo=13)
    resposta3.valor = '3'
    resposta3.descricao = 'Não tenho ciência'
    resposta3.acao = '/api/v1/chatbot/sintomasgerais'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)

    return pergunta
