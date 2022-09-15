"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from parqueadero.view import vehicleViews, webPageViews
from parqueadero.view import ticketViews
from parqueadero.view import cashViews
from parqueadero.view import parkingLotViews
from parqueadero.view import bayViews
from parqueadero.view import tariffViews
from parqueadero.view import typeVehicleViews, personViews, userView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paginaPrincipal/', webPageViews.webPage, name='principal'),
    path('login/', userView.loginView, name='login'),
    path('registerUser/', userView.register, name='registerUser'),
    path('logout/', userView.logoutView, name="logout"),
    path('prueba/', webPageViews.prueba),




    path('createTicketEntry/', ticketViews.createTicketEntry, name="ticketEntry"),
    path('generarTicketExit/<int:id>', ticketViews.ListTi.as_view(), name="generarTicketExit"),
    path('generarTicketEntry/<int:id>', ticketViews.ListTiEntry.as_view(), name="generarTicketEntry"),
    path('generarReportes/', ticketViews.ListPDF.as_view(), name="generarPDF"),
    url(r'^createTicketExit/(?P<id>\d+)/$', ticketViews.createTicketExit, name="ticketExit"),

    path('createParkingLots/', parkingLotViews.createParkingLot, name="createParkingLot"),
    path('listParkingLots/', parkingLotViews.listParkingLots, name="listParkingLot"),
    path('searchParkingLots/', parkingLotViews.searchParkingLots, name="searchParkingLots"),
    url(r'^editParkingLots/(?P<id>\d+)/$', parkingLotViews.editParkingLots, name="editParkingLots"),
    path('deleteParkingLots/<int:id>', parkingLotViews.deleteParkingLots, name="deleteParkingLots"),

    path('createBay/', bayViews.createBay, name="createBay"),
    path('listBay/', bayViews.listBays, name="listBay"),
    path('searchBay/', bayViews.searchBay, name="searchBay"),
    url(r'^editBays/(?P<id>\d+)/$', bayViews.editBays, name="editBays"),
    path('deleteBays/<int:id>', bayViews.deleteBays, name="deleteBays"),

    path('createCash/', cashViews.createCash, name='saveCash'),
    url(r'^squareBox/(?P<id>\d+)/$', cashViews.squareBox, name='squareBox'),
    path('listCash/', cashViews.listCash, name="listCash"),
    path('searchCash/', cashViews.searchCash, name="searchCash"),
    path('cuadrarCaja/<int:id>', cashViews.ListCash.as_view(), name="generarCash"),
    url(r'^editCash/(?P<id>\d+)/$', cashViews.editCash, name="editCash"),
    path('deleteCash/<int:id>', cashViews.deleteCash, name="deleteCash"),

    path('createPerson/', personViews.createPerson, name='createPerson'),
    path('listPersons/', personViews.listPerson, name="listPerson"),
    path('searchPerson/', personViews.searchPerson, name="searchPerson"),
    url(r'^editPerson/(?P<id>\d+)/$', personViews.editPerson, name="editPerson"),
    path('deletePerson/<int:id>', personViews.deletePerson, name="deletePerson"),

    path('enterVehicle/', vehicleViews.enterVehicle, name="enterVehicle"),
    path('listVehicles/', vehicleViews.listVehicles, name="listVehicles"),
    path('searchVehicle/', vehicleViews.searchVehicle, name="searchVehicle"),
    url(r'^editVehicles/(?P<id>\d+)/$', vehicleViews.editVehicle, name="editVehicle"),
    path('deleteVehicles/<int:id>', vehicleViews.deleteVehicle, name="deleteVehicle"),

    path('createTypeVehicle/', typeVehicleViews.createVehicleType, name="createVType"),
    path('listTypeVehicle/', typeVehicleViews.listTypeVehicle, name="listTypeVehicle"),
    url(r'^editTypeVehicle/(?P<id>\d+)/$', typeVehicleViews.editTypeVehicle, name="editTypeVehicle"),
    path('deleteTypeVehicle/<int:id>', typeVehicleViews.deleteTypeVehicle, name="deleteTypeVehicle"),

    path('createTariff/', tariffViews.createTariff, name="createTariff"),
    path('listTariff/', tariffViews.listTariff, name="listTariff"),
    url(r'^editTariff/(?P<id>\d+)/$', tariffViews.editTariff, name="editTariff"),
    path('deleteTariff/<int:id>', tariffViews.deleteTariff, name="deleteTariff"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
