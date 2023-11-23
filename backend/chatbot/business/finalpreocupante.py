from ..models import Pergunta, Resposta


def obterFinalPreocupante():
    pergunta, created = Pergunta.objects.get_or_create(codigo=7)
    pergunta.titulo = 'Com base nas suas respostas, indicamos que procure um oncologista para lhe ' \
                      'avaliar melhor. Espero que não seja nada grave!'

    resposta1, created = Resposta.objects.get_or_create(codigo=18)
    resposta1.valor = '1'
    resposta1.descricao = 'Voltar para o menu principal'
    resposta1.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    pergunta.respostas.add(resposta1)

    return pergunta
