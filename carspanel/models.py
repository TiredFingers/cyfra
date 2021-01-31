from django.db import models


class CarModel(models.Model):
    name = models.TextField()
    load_capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    number = models.TextField()
    model = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING)
    current_load = models.IntegerField()
    coords = models.CharField(default='', max_length=100)
    sio2 = models.IntegerField(default=0)
    fe = models.IntegerField(default=0)
    #xcoord = models.IntegerField(default=0)
    #ycoord = models.IntegerField(default=0)

    @property
    def overload(self):
        res = (self.current_load * 100) / self.model.load_capacity
        return 0 if res <= 100 else int(res - 100)

    def __str__(self):
        return str(self.model) + " " + str(self.number)


class OreStore(models.Model):
    name = models.TextField()
    current_volume = models.IntegerField()
    sio2 = models.IntegerField(default=0)
    fe = models.IntegerField(default=0)
    wkt_coords = models.TextField(default="")

    def __str__(self):
        return str(self.name)
