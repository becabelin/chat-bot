from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import PerguntaSerializer
from django.http.response import JsonResponse
from .business import principal, plataforma, suporte, cancelamento

@api_view(['GET'])
def obterMenuPrincipal(request):
    perguntaPrincipal = principal.obterMenuPrincipal()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterMenuPlataforma(request):
    perguntaPrincipal = principal.obterMenuPlataforma()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterMenuSuporte(request):
    perguntaPrincipal = principal.obterMenuSuporte()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterMenuCancelamento(request):
    perguntaPrincipal = principal.obterMenuCancelamento()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterPlataformaInicio(request):
    perguntaPrincipal = plataforma.obterIncio()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterPlataformaExercicios(request):
    perguntaPrincipal = plataforma.obterExercicios()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterPlataformaVideos(request):
    perguntaPrincipal = plataforma.obterVideos()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterPlataformaTempo(request):
    perguntaPrincipal = plataforma.obterTempo()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterPlataformaAdicionais(request):
    perguntaPrincipal = plataforma.obterAdicionais()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterSuporteProblemas(request):
    perguntaPrincipal = suporte.obterSuporteProblemas()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)

@api_view(['GET'])
def obterCancelamentoPolitica(request):
    perguntaPrincipal = cancelamento.obterCancelamentoPolitica()
    perguntaPrincipalSerializer = PerguntaSerializer(perguntaPrincipal)
    return JsonResponse(perguntaPrincipalSerializer.data)
