from rest_framework import serializers
from .models import Autor
from .models import Editora
from .models import Livro

   


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__' #vai chamar todos os arquivos TEM QUE TER DUAS ANDER LINE (__)
    

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'


class LivroSerializer(serializers.ModelSerializer):


    class Meta:
        model = Livro
        fields = '__all__'
