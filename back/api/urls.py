from django.urls import path
from .views import*
# from .views import AutoresView, listar_autores
#from .views import EditoraView, listar_editores
#from .views import LivroVieW, listar_livros

urlpatterns = [
    
    # Autores
     path('autores', AutoresView.as_view()),
    # path('authors', listar_autores),
    
    ### GET e POST

     # Editora
     path('editores', EditoraView.as_view()),
    # path('publisher', listar_editores),
    
     # Livros
    path('livros', LivroVieW.as_view()),
    #path('book', listar_livros),

    
    ### UPDATE e DELETE
    path('autor/<int:pk>',AutoresDetailView.as_view()),
    path('editora/<int:pk>', EditoraDetailView.as_view()),
    path('livro/<int:pk>', LivroDetaiVieW.as_view()),
]
