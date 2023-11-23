from ..models import Pergunta, Resposta


def obterMenuPrincipal():
    pergunta, created = Pergunta.objects.get_or_create(codigo=1)
    pergunta.titulo = 'Bem vindo ao nosso chatbot! Digite 1 para começar o teste!'

    resposta1, created = Resposta.objects.get_or_create(codigo=1)
    resposta1.valor = '1'
    resposta1.descricao = 'Iniciar teste'
    resposta1.acao = '/api/v1/chatbot/sintomasgerais'

    pergunta.save()
    resposta1.save()
    pergunta.respostas.add(resposta1)

    return pergunta