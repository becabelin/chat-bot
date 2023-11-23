from ..models import Pergunta, Resposta


def obterSintomasGerais():
    pergunta, created = Pergunta.objects.get_or_create(codigo=2)
    pergunta.titulo = 'Sintomas Gerais, você está teve ou está com algum dos sintomas abaixo?'

    resposta1, created = Resposta.objects.get_or_create(codigo=2)
    resposta1.valor = '1'
    resposta1.descricao = 'Dor'
    resposta1.acao = '/api/v1/chatbot/sintomasespecificosnao'

    resposta2, created = Resposta.objects.get_or_create(codigo=3)
    resposta2.valor = '2'
    resposta2.descricao = 'Perda de peso significativa'
    resposta2.acao = '/api/v1/chatbot/sintomasespecificosnao'

    resposta3, created = Resposta.objects.get_or_create(codigo=4)
    resposta3.valor = '3'
    resposta3.descricao = 'Fadiga'
    resposta3.acao = '/api/v1/chatbot/sintomasespecificosnao'

    resposta4, created = Resposta.objects.get_or_create(codigo=5)
    resposta4.valor = '4'
    resposta4.descricao = 'Nenhum dos sintomas'
    resposta4.acao = '/api/v1/chatbot/sintomasespecificossim'

    resposta5, created = Resposta.objects.get_or_create(codigo=6)
    resposta5.valor = '5'
    resposta5.descricao = 'Mais de um sintoma'
    resposta5.acao = '/api/v1/chatbot/sintomasespecificosnao'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    resposta4.save()
    resposta5.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)
    pergunta.respostas.add(resposta4)
    pergunta.respostas.add(resposta5)

    return pergunta
