from django.shortcuts import get_object_or_404, render, redirect
import matplotlib.pyplot as plt
from .models import Productos
from django.db.models import Count
import matplotlib; matplotlib.use('Agg')

# Create your views here.
def registro(request):
    if request.method == 'POST':
        mayor_de_edad=request.POST['mayor_de_edad']
        sabor_p=request.POST['sabor_p']
        calidad_p=request.POST['calidad_p']
        formato_p=request.POST['formato_p']
        recomendar_p=request.POST['recomendar_p']

        productos= Productos(mayor_de_edad=mayor_de_edad, sabor_p=sabor_p, calidad_p=calidad_p, formato_p=formato_p, recomendar_p=recomendar_p)
        productos.save()

        return redirect('tabla')
    else:
        return render(request, 'templates/formulario.html')
    

def tabla(request):
    productos = Productos.objects.all()
    return render(request, 'templates/tabla.html', {'productos': productos})

def graficas(request):
    productos = Productos.objects.all()
    # Obtener la cantidad de respuestas de cada pregunta
    mayor_de_edad = productos.values('mayor_de_edad').annotate(total=Count('mayor_de_edad')).order_by('-total')
    sabor_counts = productos.values('sabor_p').annotate(total=Count('sabor_p')).order_by('-total')
    calidad_counts = productos.values('calidad_p').annotate(total=Count('calidad_p')).order_by('-total')
    formato_counts = productos.values('formato_p').annotate(total=Count('formato_p')).order_by('-total')
    recomendar_counts = productos.values('recomendar_p').annotate(total=Count('recomendar_p')).order_by('-total')


    mayor_de_edad_labels = [x['mayor_de_edad'] for x in mayor_de_edad]
    mayor_de_edad_values = [x['total'] for x in mayor_de_edad]
    plt.bar(mayor_de_edad_labels, mayor_de_edad_values)
    plt.title('mayor_de_edad')
    plt.xlabel('Opciones')
    plt.ylabel('Cantidad de respuesta')
    plt.savefig('static/edad.png')
    plt.clf()


    # Crear gráficos de barras para cada pregunta
    sabor_labels = [x['sabor_p'] for x in sabor_counts]
    sabor_values = [x['total'] for x in sabor_counts]
    plt.bar(sabor_labels, sabor_values)
    plt.title('Sabor')
    plt.xlabel('Opciones')
    plt.ylabel('Cantidad de respuestas')
    plt.savefig('static/sabor.png')
    plt.clf()


    calidad_labels = [x['calidad_p'] for x in calidad_counts]
    calidad_values = [x['total'] for x in calidad_counts]
    plt.bar(calidad_labels, calidad_values)
    plt.title('Calidad')
    plt.xlabel('Opciones')
    plt.ylabel('Cantidad de respuestas')
    plt.savefig('static/calidad.png')
    plt.clf()


    formato_labels = [x['formato_p'] for x in formato_counts]
    formato_values = [x['total'] for x in formato_counts]
    plt.bar(formato_labels, formato_values)
    plt.title('Formato')
    plt.xlabel('Opciones')
    plt.ylabel('Cantidad de respuestas')
    plt.savefig('static/formato.png')
    plt.clf()


    recomendar_labels = [x['recomendar_p'] for x in recomendar_counts]
    recomendar_values = [x['total'] for x in recomendar_counts]
    plt.bar(recomendar_labels, recomendar_values)
    plt.title('Recomendar')
    plt.xlabel('Opciones')
    plt.ylabel('Cantidad de respuestas')
    plt.savefig('static/recomendar.png')
    plt.clf()

    return render(request, 'templates/graficas.html')