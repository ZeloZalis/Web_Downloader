from django.shortcuts import render
from django.http import HttpResponse
from Downloader.models import Data
from Downloader.forms import FormularioContacto

# Create your views here.
def dbSearch(request):
    return render(request, "db_search.html")

def insideCheck(request):
    
    if request.GET["prd"]:
        name = request.GET["prd"]
        if len(name) < 10:
            web_get = Data.objects.filter(website__icontains = name)
            return render(request, "results.html", {"web_get":web_get, "query":name})
        else:
            error = "El texto ingresado supera el límite."
            return render(request, "db_search.html", {"error":error})
    else:
        error = "No ha introducido nada en la búsqueda."
        return render(request, "db_search.html", {"error":error})