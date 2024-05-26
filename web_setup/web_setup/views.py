from django.http import HttpResponse
from django.template import loader

def first_page(request):
    numbers = [
        "Youtube",
        "Facebook",
        "Instagram",
        "Twitter"
    ]

    doc_template = loader.get_template("test_template.html")
    document = doc_template.render({"top_options":numbers})
    return HttpResponse(document)