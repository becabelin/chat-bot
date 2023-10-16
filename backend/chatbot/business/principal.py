from ..models import Pergunta, Resposta

def obterMenuPrincipal():
    pergunta = Pergunta()
    pergunta.titulo = 'Selecione a opção desejada'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Plataforma'
    resposta1.acao = '/api/v1/chatbot/plataforma'

    resposta2 = Resposta()
    resposta2.valor = '2'
    resposta2.descricao = 'Suporte'
    resposta2.acao = '/api/v1/chatbot/suporte'

    resposta3 = Resposta()
    resposta3.valor = '3'
    resposta3.descricao = 'cancelamento'
    resposta3.acao = '/api/v1/chatbot/cancelamento'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    resposta3.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)
    pergunta.respostas.add(resposta3)

    return pergunta

def obterMenuPlataforma():
    pergunta = Pergunta()
    pergunta.titulo = 'Selecione a opção desejada'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Como posso começar a usar a plataforma?'
    resposta1.acao = '/api/v1/chatbot/plataforma/inicio'

    resposta2 = Resposta()
    resposta2.valor = '2'
    resposta2.descricao = 'Quais tipos de exercícios estão disponíveis na plataforma?'
    resposta2.acao = '/api/v1/chatbot/plataforma/exercicios'

    resposta3 = Resposta()
    resposta3.valor = '3'
    resposta3.descricao = 'Há vídeos de instruções para os exercícios?'
    resposta3.acao = '/api/v1/chatbot/plataforma/videos'

    resposta4 = Resposta()
    resposta4.valor = '4'
    resposta4.descricao = 'Quanto tempo de exercício é recomendado por dia/semana?'
    resposta4.acao = '/api/v1/chatbot/plataforma/tempo'

    resposta5 = Resposta()
    resposta5.valor = '5'
    resposta5.descricao = 'Quais recursos adicionais a plataforma oferece para promover um estilo de vida saudável?'
    resposta5.acao = '/api/v1/chatbot/plataforma/adicionais'

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


def obterMenuSuporte():
    pergunta = Pergunta()
    pergunta.titulo = 'Selecione a opção desejada'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Como posso solucionar problemas técnicos na plataforma?'
    resposta1.acao = '/api/v1/chatbot/suporte/problemas'

    pergunta.save()
    resposta1.save()
    pergunta.respostas.add(resposta1)

    return pergunta


def obterMenuCancelamento():
    pergunta = Pergunta()
    pergunta.titulo = 'Selecione a opção desejada'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Qual é a política de cancelamento da assinatura?'
    resposta1.acao = '/api/v1/chatbot/cancelamento/politica'

    pergunta.save()
    resposta1.save()
    pergunta.respostas.add(resposta1)

    return pergunta
