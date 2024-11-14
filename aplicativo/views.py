from django.shortcuts import render

from aplicativo.models import Car

# Create your views here.
def index(request):
    cars = Car.objects.all()
    return render(request, 'index.html', {'cars': cars})