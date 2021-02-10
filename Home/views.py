from django.shortcuts import render, HttpResponse, redirect
from Home.forms import FormCourse
from Home.models import Career, Course
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango',
    })

# Listar cursos 🎇


def list_courses(request):
    cursos = Course.objects.all()
    return render(request, 'list_courses.html', {
        'cursos': cursos,
        'titulo': 'Listado de Cursos'
    })


def delete_course(request, id):
    curso = Course.objects.get(pk=id)
    curso.delete()
    return redirect('list_courses')


def save_course(request):
    if request.method == 'POST':
        code = request.POST['codigo']
        name = request.POST['nombre']
        hour = request.POST['horas']
        state = request.POST['estado']

        curso = Course(
            code=code,
            name=name,
            hour=hour,
            state=state
        )
        curso.save()
        return HttpResponse("""
                            <script> 
                            alert("Curso registrado con exito")
                            </script>
                            """)
    else:
        return HttpResponse("alert('Error al crear curso')")


def create_course(request):
    return render(request, 'create_course.html')


# Listar carreras 🎇


def list_careers(request):
    carreras = Career.objects.all()
    return render(request, 'list_careers.html', {
        'carreras': carreras,
        'titulo': 'Listado de Carreras'
    })


def delete_career(request, id):
    carrera = Career.objects.get(pk=id)
    carrera.delete()
    return redirect('list_careers')


def save_career(request):
    if request.method == 'POST':
        name = request.POST['nombre']
        shortname = request.POST['sobrenombre']
        state = request.POST['estado']
        imagen = request.POST['img']
        curso = Career(
            name=name,
            shortname=shortname,
            state=state,
            imagen=imagen
        )
        curso.save()
        return redirect('list_careers')
    else:
        return HttpResponse("alert('Error al crear carrera')")


def create_career(request):
    return render(request, 'create_career.html')