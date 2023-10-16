from ..models import Pergunta, Resposta

def obterCancelamentoPolitica():
    pergunta, created = Pergunta.objects.get_or_create(codigo=11)
    pergunta.titulo = 'Qual é a política de cancelamento da assinatura?'

    resposta1, created = Resposta.objects.get_or_create(codigo=23)
    resposta1.valor = '23'
    resposta1.descricao = 'O pagamento da assinatura Fit.Nez é feito pela sua empresa empregadora. Caso você não tenha mais interesse em utilizar a plataforma, entre em contato com o RH da sua empresa e os comunique imediatamente.'

    resposta2, created = Resposta.objects.get_or_create(codigo=24)
    resposta2.valor = '24'
    resposta2.descricao = 'Voltar ao menu principal'
    resposta2.acao = '/api/v1/chatbot/principal'

    pergunta.save()
    resposta1.save()
    resposta2.save()
    pergunta.respostas.add(resposta1)
    pergunta.respostas.add(resposta2)

    return pergunta
