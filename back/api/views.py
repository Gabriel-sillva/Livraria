from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Autor
from .models import Editora
from .models import Livro
from .serializers import AutorSerializer
from .serializers import EditoraSerializer
from .serializers import LivroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Filters



# Autores
class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

@api_view(['GET', 'POST'])
def listar_autores(request):
    if request.method  == 'GET':
        queryset = Autor.objects.all()
        serializer = AutorSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AutorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

# Editores
class EditoraView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

@api_view(['GET', 'POST'])
def listar_editores(request):
    if request.method == 'GET':
        queryset = Editora.objects.all()
        serializer = EditoraSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EditoraSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        

# Livros
class LivroVieW(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

@api_view(['GET', 'POST'])
def listar_livros(Request):
    if Request.method == 'GET':
        queryset = Livro.objects.all()
        serializer = LivroSerializer(queryset, many=True)
        return Response(serializer.data)
    elif Request.method == 'POST':
        serializer = LivroSerializer(data = Request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        


# %%%%%%%%%%%%%%%%%%%% Autores %%%%%%%%%%%%%%%%%%%%

class AutoresView(ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class AutoresDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

# %%%%%%%%%%%%%%%%%%%% Editores %%%%%%%%%%%%%%%%%%%%

class EditoraView(ListCreateAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

class EditoraDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

# %%%%%%%%%%%%%%%%%%%% Livros %%%%%%%%%%%%%%%%%%%%

class LivroDetaiVieW(RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroVieW(ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer