from django.db import models

class Cash(models.Model):
    name = models.CharField(max_length=100)
    base_money = models.IntegerField()
    total_income = models.IntegerField()
    total_money = models.IntegerField()
    user = models.CharField(max_length=100)
    opening_date = models.DateTimeField(max_length=100)
    closing_date = models.DateTimeField(max_length=100, null=True)
    state = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cash'


class ParkingLot(models.Model):

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imagesParking')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parkinglot'

class Bay(models.Model):
    par_id = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    available = models.BooleanField()

    def __str__(self):
        return self.number

    class Meta:
        db_table = 'bay'



class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    doc_number = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'person'


class Tariff(models.Model):
    cost = models.IntegerField()

    def __str__(self):
        return str(self.cost)

    class Meta:
        db_table = 'tariff'


class TypeVehicle(models.Model):
    tariff_id = models.ForeignKey(Tariff, on_delete=models.CASCADE)
    vehicle_class = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.vehicle_class

    class Meta:
        db_table = 'typevehicle'



class Vehicle(models.Model):
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    typevehicle_id = models.ForeignKey(TypeVehicle, on_delete=models.CASCADE)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=50)
    vehicle_photo = models.ImageField(upload_to='imagesCar')


    def __str__(self):
        return self.license_plate

    class Meta:
        db_table = 'vehicle'


class Ticket(models.Model):
    cash_id = models.ForeignKey(Cash, on_delete=models.CASCADE)
    bay_id = models.ForeignKey(Bay, on_delete=models.CASCADE, null=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    entry_time = models.DateTimeField(max_length=100)
    total_time= models.FloatField(null=True)
    departure_time = models.DateTimeField(max_length=100, null=True)
    cost = models.FloatField(null=True)
    date = models.DateField(max_length=100)

    def __str__(self):
        return self.cost

    class Meta:
        db_table = 'ticket'


