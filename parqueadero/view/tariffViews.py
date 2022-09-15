from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from parqueadero.models import Tariff, ParkingLot, TypeVehicle
from parqueadero.forms import tariffForm

@login_required()
@permission_required('parqueadero.view_tariff')
def listTariff(request):
    list= TypeVehicle.objects.all()
    parqueadero = ParkingLot.objects.all()
    return render(request, 'tariffs/listTariff.html', {'list':list, 'parqueadero':parqueadero})

@login_required()
@permission_required('parqueadero.add_tariff')
def createTariff(request):
    form = tariffForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return  render(request, "tariffs/createTariff.html", context);

@login_required()
@permission_required('parqueadero.change_tariff')
def editTariff(request, id):
    editTariff = Tariff.objects.get(id=id)
    form = tariffForm(request.POST or None, instance=editTariff)
    if form.is_valid():
        form.save()
        return redirect('/listTariff/')

    context = {
        'form': form
    }
    return render(request, "persons/createPerson.html", context);

@login_required()
@permission_required('parqueadero.delete_tariff')
def deleteTariff(request, id):
    post = Tariff.objects.get(pk=id)
    post.delete()
    return redirect("listTariff")

