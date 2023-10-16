from ..models import Pergunta, Resposta

def obterIncio():
    pergunta, created = Pergunta.objects.get_or_create(codigo=6)
    pergunta.titulo = 'Como posso começar a usar a plataforma?'

    resposta1, created = Resposta.objects.get_or_create(codigo=13)
    resposta1.valor = '13'
    resposta1.descricao = 'Você receberá um e-mail com as instruções de acesso. O login em nossa plataforma é feito através do e-mail corporativo e de uma senha que você criará.'

    resposta2, created = Resposta.objects.get_or_create(codigo=14)
    resposta2.valor = '14'
    resposta2.descricao = 'Voltar ao menu principal'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta

def obterExercicios():
    pergunta, created = Pergunta.objects.get_or_create(codigo=7)
    pergunta.titulo = 'Quais tipos de exercícios estão disponíveis na plataforma?'

    resposta1, created = Resposta.objects.get_or_create(codigo=15)
    resposta1.valor = '15'
    resposta1.descricao = 'Nossa plataforma possui diversos exercícios para acompanhamento, entre eles estão: alongamento, corrida, caminhada, ciclismo, musculação, zumba, fit dance, crossfit, calistenia, natação, futebol e vôlei. Em breve traremos mais exercícios.'

    resposta2, created = Resposta.objects.get_or_create(codigo=16)
    resposta2.valor = '16'
    resposta2.descricao = 'Voltar ao menu principal.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta

def obterVideos():
    pergunta, created = Pergunta.objects.get_or_create(codigo=8)
    pergunta.titulo = 'Há vídeos de instruções para os exercícios?'

    resposta1, created = Resposta.objects.get_or_create(codigo=17)
    resposta1.valor = '17'
    resposta1.descricao = 'No momento não, mas estamos trabalhando na criação de diversos materiais para auxiliar nossos usuários a manterem um estilo de vida saudável.'

    resposta2, created = Resposta.objects.get_or_create(codigo=18)
    resposta2.valor = '18'
    resposta2.descricao = 'Voltar ao menu principal.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta

def obterTempo():
    pergunta, created = Pergunta.objects.get_or_create(codigo=9)
    pergunta.titulo = 'Quanto tempo de exercício é recomendado por dia/semana?'

    resposta1, created = Resposta.objects.get_or_create(codigo=19)
    resposta1.valor = '19'
    resposta1.descricao = 'Recomendamos a prática de exercícios de intensidade moderada por no mínimo meia hora por dia.'

    resposta2, created = Resposta.objects.get_or_create(codigo=20)
    resposta2.valor = '20'
    resposta2.descricao = 'Voltar ao menu principal.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta

def obterAdicionais():
    pergunta, created = Pergunta.objects.get_or_create(codigo=10)
    pergunta.titulo = 'Quais recursos adicionais a plataforma oferece para promover um estilo de vida saudável?'

    resposta1, created = Resposta.objects.get_or_create(codigo=21)
    resposta1.valor = '21'
    resposta1.descricao = 'Em breve lançaremos novos recursos em nossa plataforma, dentre elas, uma ferramenta para agendamento de consulta com personal trainer e nutricionista por videochamada.'

    resposta2, created = Resposta.objects.get_or_create(codigo=22)
    resposta2.valor = '22'
    resposta2.descricao = 'Voltar ao menu principal.'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta
