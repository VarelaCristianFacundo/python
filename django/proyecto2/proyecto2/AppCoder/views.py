from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

# Create your views here.
def curso(req, nombre, camada):
    
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    
    return HttpResponse(f"""
                        <p>Curso: {curso.nombre} - Camada: {curso.camada} Creado con éxito</p>                        
                        """)
    
def listar_cursos(req):
    lista = Curso.objects.all()
    
    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):
    return render(req, "inicio.html")

def cursos(req):
    return render(req, "cursos.html")

def profesores(req):
    return render(req, "profesores.html")

def estudiantes(req):    
    return render(req, "estudiantes.html")

def entregables(req): 
    return render(req, "entregables.html")

def login(req): 
    return render(req, "login.html")

def cursoFormulario(req):    
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        pass
    else:
        return render(req, "cursoFormulario.html")
    return render(req, "cursoFormulario.html")