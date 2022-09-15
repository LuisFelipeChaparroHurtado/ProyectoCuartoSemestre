from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from parqueadero.models import ParkingLot
from parqueadero.forms import parkingLotForm
from django.contrib.auth import authenticate, login, logout

@login_required()
@permission_required('parqueadero.view_parkinglot')
def listParkingLots(request):
    list = ParkingLot.objects.all()
    return render(request, "parkingLot/listParkingLots.html", {'list':list})

@login_required()
@permission_required('parqueadero.add_parkinglot')
def createParkingLot(request):
    if request.method == 'POST':
        form = parkingLotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'parkingLot/createParkingLot.html', {'form': form, 'img_obj': img_obj})

    else:
        form = parkingLotForm()
    return render(request, 'parkingLot/createParkingLot.html', {'form': form})

@login_required()
def searchParkingLots(request):
    search = request.POST.get('search',False)
    filter = ParkingLot.objects.filter(name__startswith=search)
    return render(request, 'parkingLot/listParkingLots.html', {'list':filter})

@login_required()
@permission_required('parqueadero.change_parkinglot')
def editParkingLots(request, id):
    editBay = ParkingLot.objects.get(id=id)
    form = parkingLotForm(request.POST or None, instance=editBay)
    if form.is_valid():
        form.save()
        return redirect('/listParkingLots/')

    context = {
        'form': form
    }
    return render(request, "parkingLot/createParkingLot.html", context);

@login_required()
@permission_required('parqueadero.delete_parkinglot')
def deleteParkingLots(request, id):
    post = ParkingLot.objects.get(pk=id)
    post.delete()
    return redirect("listParkingLot")
