from ..models import Pergunta, Resposta

def obterIncio():
    pergunta = Pergunta()
    pergunta.titulo = 'Como posso começar a usar a plataforma?'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Você receberá um e-mail com as instruções de acesso. O login em nossa plataforma é feito através do e-mail corporativo e de uma senha que você criará.'

    resposta2 = Resposta()
    resposta2.valor = '2'
    resposta2.descricao = 'Caso queira voltar ao menu principal, digite 2.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta

def obterExercicios():
    pergunta = Pergunta()
    pergunta.titulo = 'Quais tipos de exercícios estão disponíveis na plataforma?'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Nossa plataforma possui diversos exercícios para acompanhamento, entre eles estão: alongamento, corrida, caminhada, ciclismo, musculação, zumba, fit dance, crossfit, calistenia, natação, futebol e vôlei. Em breve traremos mais exercícios.'

    resposta2 = Resposta()
    resposta2.valor = '2'
    resposta2.descricao = 'Caso queira voltar ao menu principal, digite 2.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta

def obterVideos():
    pergunta = Pergunta()
    pergunta.titulo = 'Há vídeos de instruções para os exercícios?'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'No momento não, mas estamos trabalhando na criação de diversos materiais para auxiliar nossos usuários a manterem um estilo de vida saudável.'

    resposta2 = Resposta()
    resposta2.valor = '2'
    resposta2.descricao = 'Caso queira voltar ao menu principal, digite 2.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta

def obterTempo():
    pergunta = Pergunta()
    pergunta.titulo = 'Quanto tempo de exercício é recomendado por dia/semana?'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Recomendamos a prática de exercícios de intensidade moderada por no mínimo meia hora por dia.'

    resposta2 = Resposta()
    resposta2.valor = '2'
    resposta2.descricao = 'Caso queira voltar ao menu principal, digite 2.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta
