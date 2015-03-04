from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from cats.models import Cat
from PIL import Image

def index(request):
    ctxt = {
        'cats': Cat.objects.all()
    }
    return render(request, 'cats/index.html', ctxt)

def photo(request, id):
    cat = get_object_or_404(Cat, pk=id)
    response = HttpResponse(content_type="image/png")
    img = Image.open(cat.image)
    img.save(response, 'png')
    return response
