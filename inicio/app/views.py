from django.shortcuts import render

from .models import Usuarios

# Create your views here.


def index(request):

    return render(request,'cadastro.html')

def usuarios(request):
   
   id_usuarios = Usuarios()

   id_usuarios.nome = request.POST.get('nome')

   id_usuarios.idade = request.POST.get('idade')

   id_usuarios.cpf = request.POST.get('cpf')

   id_usuarios.save()
    
   usuarios = {
       
       'usuarios':Usuarios.objects.all(),

   }
   

   return render(request,'mostra.html',usuarios)


