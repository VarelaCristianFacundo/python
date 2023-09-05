from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso
from .forms import CursoFormulario

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
    if req.method == 'POST':
        cursoFormulario = CursoFormulario(req.POST)
        
        if cursoFormulario.is_valid():        
            data = cursoFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
            
            return render(req, "cursoFormulario.html")
    else:
        cursoFormulario = CursoFormulario()                

    print(cursoFormulario)    
    return render(req, "cursoFormulario.html", {"cursoFormulario": cursoFormulario})

def busquedaCamada(req):
    return render(req, "busquedaCamada.html")

def buscar(req):
    
    if req.GET["camada"]:
        camada = req.GET["camada"]    
        curso = Curso.objects.get(camada=camada)
        return render(req, "resultadoBusqueda.html", {"curso": curso})
    else:        
        return HttpResponse(f'Debe agregar una camada')