from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from parqueadero.models import Vehicle, ParkingLot
from parqueadero.models import Ticket
from parqueadero.forms import vehicleForm
from django.contrib.auth import authenticate, login, logout

@login_required()
@permission_required('parqueadero.view_vehicle')
def listVehicles(request):
    nameParking = ParkingLot.objects.all()
    ticket = Ticket.objects.all()
    return render(request, 'vehicles/listVehicles.html', {'ListV': ticket, "parqueadero": nameParking})

def searchVehicle(request):
    nameParking = ParkingLot.objects.all()
    search = request.POST.get('search',False)
    filter = Ticket.objects.filter(vehicle_id__license_plate__startswith=search)
    return render(request, 'vehicles/listVehicles.html', {'ListV':filter, "parqueadero":nameParking})

@login_required()
@permission_required('parqueadero.add_vehicle')
def enterVehicle(request):
    if request.method == 'POST':
        form = vehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'vehicles/enterVehicle.html', {'form': form, 'img_obj': img_obj})

    else:
        form = vehicleForm()
    return render(request, 'vehicles/enterVehicle.html', {'form': form})

@login_required()
@permission_required('parqueadero.change_vehicle')
def editVehicle(request, id):
    editVehicles = Vehicle.objects.get(id=id)
    form = vehicleForm(request.POST or None, instance=editVehicles)
    if form.is_valid():
        form.save()
        return redirect('/listVehicles/')

    context = {
        'form': form
    }
    return render(request, "vehicles/enterVehicle.html", context);

@login_required()
@permission_required('parqueadero.delete_vehicle')
def deleteVehicle(request, id):
    post = Vehicle.objects.get(pk=id)
    post.delete()
    return redirect("listVehicles")