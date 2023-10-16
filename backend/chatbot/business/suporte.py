from ..models import Pergunta, Resposta

def obterSuporteProblemas():
    pergunta = Pergunta()
    pergunta.titulo = 'Como posso solucionar problemas técnicos na plataforma?'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'Em casos de problemas na plataforma, você pode conversar com nossos especialistas através do número (11) 98765-4321 ou por e-mail através do suporte@fitnez.com.br. Nossos especialistas estão disponíveis de segunda a sexta, das 08h às 17h.'

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
