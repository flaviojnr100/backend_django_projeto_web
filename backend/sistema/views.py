from http import HTTPStatus

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from .models import Pessoa
# Create your views here.
from .serializer import PessoaSerializer

@api_view(['GET'])

def getPessoas(request):
    serializer = PessoaSerializer(Pessoa.objects.all().order_by('id'), many=True)
    return JsonResponse(serializer.data,safe=False)


@api_view(['POST'])
def createPessoa(request):
    serializer = PessoaSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=HTTPStatus.CREATED)
    return JsonResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

@api_view(['PUT'])
def editPessoa(request,pk):
    pessoa = get_object_or_404(Pessoa.objects.all(), pk=pk)
    if pessoa:
        serializer = PessoaSerializer(pessoa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=HTTPStatus.ACCEPTED)
        return JsonResponse(serializer.errors, status=HTTPStatus.NOT_FOUND)

@api_view(['DELETE'])
def deletePessoa(request,pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if pessoa:
        pessoa.delete()
        return HttpResponse(status=HTTPStatus.ACCEPTED)
    return HttpResponse(status=HTTPStatus.NOT_FOUND)



