from ..models import Pergunta, Resposta

def obterCancelamentoPolitica():
    pergunta = Pergunta()
    pergunta.titulo = 'Qual é a política de cancelamento da assinatura?'

    resposta1 = Resposta()
    resposta1.valor = '1'
    resposta1.descricao = 'O pagamento da assinatura Fit.Nez é feito pela sua empresa empregadora. Caso você não tenha mais interesse em utilizar a plataforma, entre em contato com o RH da sua empresa e os comunique imediatamente.'

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
