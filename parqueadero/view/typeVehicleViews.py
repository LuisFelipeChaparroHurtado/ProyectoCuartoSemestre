from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect
from parqueadero.models import TypeVehicle, ParkingLot, Ticket
from parqueadero.forms import typeVehicleForm

@login_required()
@permission_required('parqueadero.view_typevehicle')
def listTypeVehicle(request):
    list = TypeVehicle.objects.all()
    parqueadero = ParkingLot.objects.all()
    return render(request, "typeVehicles/listTypeVehicle.html", {'list':list, 'parqueadero':parqueadero})

@login_required()
@permission_required('parqueadero.add_typevehicle')
def createVehicleType(request):
    form = typeVehicleForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return  render(request, "typeVehicles/createTypeVehicle.html", context);

@login_required()
def searchTypeVehicle(request):
    search = request.POST.get('search',False)
    filter = TypeVehicle.objects.filter(name__startswith=search)
    return render(request, 'typeVehicles/listTypeVehicle.html', {'list':filter})

@login_required()
@permission_required('parqueadero.change_typevehicle')
def editTypeVehicle(request, id):
    editTypeVehicle = TypeVehicle.objects.get(id=id)
    form = typeVehicleForm(request.POST or None, instance=editTypeVehicle)
    if form.is_valid():
        form.save()
        return redirect('/listTypeVehicle/')

    context = {
        'form': form
    }
    return render(request, "typeVehicles/createTypeVehicle.html", context);

@login_required()
@permission_required('parqueadero.delete_typevehicle')
def deleteTypeVehicle(request, id):
    post = TypeVehicle.objects.get(pk=id)
    post.delete()
    return redirect("listTypeVehicle")