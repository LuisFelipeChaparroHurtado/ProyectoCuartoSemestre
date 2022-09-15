from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect
from parqueadero.models import ParkingLot, Ticket,Person
from parqueadero.forms import personForm


@login_required()
@permission_required('parqueadero.view_person')
def listPerson(request):
    ticket = Ticket.objects.all()
    parqueadero = ParkingLot.objects.all()
    return render(request, "persons/listPerson.html", {'parqueadero':parqueadero, 'ticket':ticket})

@login_required()
@permission_required('parqueadero.add_person')
def createPerson(request):

    form = personForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("enterVehicle")

    context = {
        'form' : form
    }
    return  render(request, "persons/createPerson.html", context);

@login_required()
def searchPerson(request):
    parqueadero = ParkingLot.objects.all()
    search = request.POST.get('search',False)
    filter = Ticket.objects.filter(vehicle_id__person_id__name__startswith=search)
    return render(request, 'persons/listPerson.html', {'parqueadero':parqueadero, 'ticket':filter})

@login_required()
@permission_required('parqueadero.change_person')
def editPerson(request, id):
    editPersons = Person.objects.get(id=id)
    form = personForm(request.POST or None, instance=editPersons)
    if form.is_valid():
        form.save()
        return redirect('/listPersons/')

    context = {
        'form': form
    }
    return render(request, "persons/createPerson.html", context);

@login_required()
@permission_required('parqueadero.delete_person')
def deletePerson(request, id):
    post = Person.objects.get(pk=id)
    post.delete()
    return redirect("listPerson")