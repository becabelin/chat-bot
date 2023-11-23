from ..models import Pergunta, Resposta


def obterSintomasEspecificos():
    pergunta, created = Pergunta.objects.get_or_create(codigo=3)
    pergunta.titulo = 'Sintomas específicos, você está teve ou está com algum dos sintomas abaixo?'

    resposta1, created = Resposta.objects.get_or_create(codigo=7)
    resposta1.valor = '1'
    resposta1.descricao = 'Nódulo ou inchaço'
    resposta1.acao = '/api/v1/chatbot/sintomasgerais'

    resposta2, created = Resposta.objects.get_or_create(codigo=8)
    resposta2.valor = '2'
    resposta2.descricao = 'Alteração na cor ou textura da pele'
    resposta2.acao = '/api/v1/chatbot/sintomasgerais'

    resposta3, created = Resposta.objects.get_or_create(codigo=9)
    resposta3.valor = '3'
    resposta3.descricao = 'Nenhum dos sintomas'
    resposta3.acao = '/api/v1/chatbot/sintomasgerais'

    resposta4, created = Resposta.objects.get_or_create(codigo=10)
    resposta4.valor = '4'
    resposta4.descricao = 'Mais de um sintoma'
    resposta4.acao = '/api/v1/chatbot/sintomasgerais'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    resposta4.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)
    pergunta.respostas.add(resposta4)

    return pergunta
