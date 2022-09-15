from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ProyectoFinal.utils import render_to_pdf
from parqueadero.models import Ticket, Cash, Bay
from parqueadero.forms import ticketForm, ticketExitForm, vehicleForm
from django.views.generic import ListView, View

class ListTi(View):
    def get(self, request, id, *args, **kwargs):

        ticket = Ticket.objects.get(id=id)
        totalTime = (ticket.departure_time - ticket.entry_time)
        totalTime = totalTime.seconds/3600
        ticket.total_time = totalTime
        ticket.cost= ((ticket.total_time))*ticket.vehicle_id.typevehicle_id.tariff_id.cost
        cash = Cash.objects.get(id=ticket.cash_id.id)
        cash.total_income= cash.total_income +ticket.cost
        cash.total_money= cash.total_income +cash.base_money
        #cash.total_moneyBase = cash.total_money - cash.total_expenses
        bay = Bay.objects.get(id=ticket.bay_id.id)
        bay.available = True
        bay.save()
        ticket.save()
        cash.save()


        context = {
            'data':ticket,
        }
        pdf = render_to_pdf('ticketEntry/pdfTicketExit.html', context)
        return HttpResponse(pdf, content_type="application/pdf")



class ListTiEntry(View):
    def get(self, request, id, *args, **kwargs):
        ticket = Ticket.objects.get(vehicle_id_id=id)
        context = {
            'data': ticket,
        }
        pdf = render_to_pdf('ticketEntry/pdfTicketEntry.html', context)
        return HttpResponse(pdf, content_type="application/pdf")


class ListPDF(View):
    def get(self, request, *args, **kwargs):
        data = Ticket.objects.all()
        pdf = render_to_pdf('ticketEntry/lista.html', {'ticket':data})
        return HttpResponse(pdf, content_type="application/pdf")

def createTicketEntry(request):
    import pdb;

    form = ticketForm(request.POST or None)
    if form.is_valid():
            bay = form.cleaned_data['bay_id']
            vehicle = form.cleaned_data['vehicle_id']
            bay.available = False
            bay.save()
            #pdb.set_trace()
            form.save()
            return redirect('/generarTicketEntry/'+ str(vehicle.id))

    context = {
        'form' : form,
    }
    return  render(request, "ticketEntry/ticketEntry.html", context);

@login_required()
def createTicketExit(request,id):
    ticketExit = Ticket.objects.get(id=id)
    form = ticketExitForm(request.POST or None, instance=ticketExit)
    if form.is_valid():
        ticketExit.bay_id.available= False
        form.save()
        return redirect('/generarTicketExit/'+id)

    context = {
        'form': form
    }
    return render(request, "ticketEntry/ticketExit.html", context);

@login_required()
def generarPDF(request, id):
    context = {}
    context['data'] = Ticket.objects.get(id=id)
    return render(request, 'ticketEntry/pdfTicketExit.html', context)
