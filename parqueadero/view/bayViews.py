from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from parqueadero.models import Bay, ParkingLot, Vehicle
from parqueadero.forms import bayForm

@login_required()
@permission_required('parqueadero.view_bay')
def listBays(request):
    lista= Bay.objects.all()
    parqueadero= ParkingLot.objects.all()
    return render(request, "bays/listBays.html", {'lista':lista, 'parqueadero':parqueadero});

@login_required()
def searchBay(request):
    parqueadero= ParkingLot.objects.all()
    search = request.POST.get('search',False)
    filter = Bay.objects.filter(number=search)
    return render(request, 'bays/listBays.html', {'lista':filter, "parqueadero":parqueadero})

@login_required()
@permission_required('parqueadero.change_bay')
def editBays(request, id):
    editBay = Bay.objects.get(id=id)
    form = bayForm(request.POST or None, instance=editBay)
    if form.is_valid():
        form.save()
        return redirect('/listBay/')

    context = {
        'form': form
    }
    return render(request, "bays/createBay.html", context);

@login_required()
@permission_required('parqueadero.delete_bay')
def deleteBays(request, id):
    post = Bay.objects.get(pk=id)
    post.delete()
    return redirect("listBay")

@login_required()
@permission_required('parqueadero.add_bay')
def createBay(request):
    form = bayForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return  render(request, "bays/createBay.html", context);

