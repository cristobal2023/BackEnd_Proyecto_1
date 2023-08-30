from django.http import HttpResponse

#Acá se agregan las vistas

def hola(request):
    return HttpResponse("Hola bienvenidos al curso de Django")

def chao(request):
    return HttpResponse("<h2>Adios, gracias por la atención<h2>")

def verhora(request):
    return HttpResponse("Aquí colocar la hora y fecha actual")