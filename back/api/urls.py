from django.urls import path
from .views import AutoresView, listar_autores
from .views import EditoraView, listar_editores
from .views import LivroVieW, listar_livros

urlpatterns = [
    
    # Autores
     path('autores', AutoresView.as_view()),
     path('authors', listar_autores),

     # Editora
     path('editora', EditoraView.as_view()),
     path('publisher', listar_editores),
     
     # Livros
    path('livro', LivroVieW.as_view()),
    path('book', listar_livros),
]