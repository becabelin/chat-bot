from ..models import Pergunta, Resposta


def obterFumante():
    pergunta, created = Pergunta.objects.get_or_create(codigo=5)
    pergunta.titulo = 'Você é ou já foi fumante?'

    resposta1, created = Resposta.objects.get_or_create(codigo=14)
    resposta1.valor = '1'
    resposta1.descricao = 'Sim, atualmente'
    resposta1.acao = '/api/v1/chatbot/sintomasgerais'

    resposta2, created = Resposta.objects.get_or_create(codigo=15)
    resposta2.valor = '2'
    resposta2.descricao = 'Sim, mas parei'
    resposta2.acao = '/api/v1/chatbot/sintomasgerais'

    resposta3, created = Resposta.objects.get_or_create(codigo=16)
    resposta3.valor = '3'
    resposta3.descricao = 'Não'
    resposta3.acao = '/api/v1/chatbot/sintomasgerais'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)

    return pergunta
