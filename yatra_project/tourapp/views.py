from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    return render(request, "index.html", {'result': obj})


def item(request):
    team = Team.objects.all()
    return render(request, "index.html", {'team1': team})
