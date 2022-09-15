from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from parqueadero.models import Cash
from django.contrib.auth import authenticate, login, logout

@login_required()
def webPage(request):
    listaCaja = Cash.objects.all()
    return render(request,'webPage/webPage.html', {'ListCash': listaCaja})

def prueba(request):
    return render(request, "webPage/indicadorCarga.html")



