# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render

def zz_yt(request):

    return render(request, "sub_templates/youtube.html")

def first_page(request):
    numbers = [
        "Youtube",
        "Facebook",
        "Instagram",
        "Twitter"
    ]

    #Se usa el loader para cargar varios templates si es necesario, si sólo se necesita cargar uno
    #con el método render se puede hacer directamente.
    # doc_template = loader.get_template("test_template.html")
    # document = doc_template.render({"top_options":numbers})
    
    return render(request, "sub_templates/main.html", {"top_options":numbers})