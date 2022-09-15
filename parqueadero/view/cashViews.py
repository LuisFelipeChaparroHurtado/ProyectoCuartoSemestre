from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from ProyectoFinal.utils import render_to_pdf
from parqueadero.models import Cash, Ticket
from parqueadero.forms import cashForm, cashFormExit

class ListCash(View):
    def get(self, request,id, *args, **kwargs):
        data = Ticket.objects.all()
        cash = Cash.objects.get(id=id)
        context = {
            'cash' : cash,
            'data' :data
        }
        pdf = render_to_pdf('cash/pdfCash.html',  context)
        return HttpResponse(pdf, content_type="application/pdf")

@login_required()
@permission_required('parqueadero.view_cash')
def listCash(request):
    listCash = Cash.objects.all()
    return render(request, "cash/listCash.html", {'list':listCash})

@login_required()
@permission_required('parqueadero.add_cash')
def createCash(request):
    form = cashForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return  render(request, "cash/createCash.html", context);

@login_required()
def squareBox(request, id):
    cuadrarC = Cash.objects.get(id=id)
    form = cashFormExit(request.POST or None, instance=cuadrarC)
    if form.is_valid():
        form.save()
        return redirect('/cuadrarCaja/'+id)

    context = {
        'form': form
    }
    return render(request, "cash/cuadrarCash.html", context);

@login_required()
def searchCash(request):
    search = request.POST.get('search',False)
    filter = Cash.objects.filter(name__startswith=search)
    return render(request, 'cash/listCash.html', {'list':filter})

@login_required()
@permission_required('parqueadero.change_cash')
def editCash(request, id):
    editBay = Cash.objects.get(id=id)
    form = cashForm(request.POST or None, instance=editBay)
    if form.is_valid():
        form.save()
        return redirect('/listCash/')

    context = {
        'form': form
    }
    return render(request, "cash/createCash.html", context);

@login_required()
@permission_required('parqueadero.delete_cash')
def deleteCash(request, id):
    post = Cash.objects.get(pk=id)
    post.delete()
    return redirect("listParkingLot")

