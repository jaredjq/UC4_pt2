from django.shortcuts import render, HttpResponse


# Create your views here.

layout = """
    <h1> Proyecto Web (UC04) | BFJ </h1>
    <hr/>
    <ul>
        <li>
            <a href="/index"> Integrantes</a>
        </li>
        <li>
            <a href="/saludo"> Saludo</a>
        </li>
    </ul>
    <hr/>
"""


def index(request):
    estudiantes = [ 'Bonifacio Toledo, Dharma Elizabeht', 
                    'Flores Mayta, Rodrigo Melecio',
                    'Jimenez Quispe, Hubert Jared']


    return render(request,'integrantes.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web Con DJango',
        'estudiantes': estudiantes
    })




def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'SI'
    })
