from django.shortcuts import render, redirect, reverse
from .models import Car, OreStore
from .forms import CarForm
from django.forms import modelformset_factory, formset_factory
from shapely.geometry import Point, Polygon
import json


def index(req):

    cars = Car.objects.all()

    return render(req, "carspanel/index.html", {'cars': cars, 'len_cars': len(cars)})


def calc_store_load(req):

    CarFormSet = formset_factory(CarForm)

    formset = CarFormSet(req.POST)

    if formset.is_valid():
        data = formset.cleaned_data
        store = OreStore.objects.first()

        store_coords = json.loads(store.wkt_coords)

        poly = Polygon(store_coords)

        store_fe_weight = (store.current_volume * store.fe) / 100
        store_sio2_weight = (store.current_volume * store.sio2) / 100

        new_store_fe = store.fe
        new_store_sio2 = store.sio2
        volume_after_unload = store.current_volume

        for row in data:
            point = Point([int(coord) for coord in row['coords'].split(" ")])

            if point.within(poly):

                car = Car.objects.filter(id=int(row['car'])).first()

                if car:
                    volume_after_unload += car.current_load
                    car_fe_weight = (car.current_load * car.fe) / 100
                    car_sio2_weight = (car.current_load * car.sio2) / 100

                    new_store_fe = ((store_fe_weight + car_fe_weight) / volume_after_unload) * 100
                    new_store_sio2 = ((store_sio2_weight + car_sio2_weight) / volume_after_unload) * 100

                    store_fe_weight += car_fe_weight
                    store_sio2_weight += car_sio2_weight

        return render(req, "carspanel/store.html", {'store': store, 'volume': store.current_volume,
                                                    'volume_after_unload': volume_after_unload,
                                                    'new_store_fe': new_store_fe,
                                                    'new_store_sio2': new_store_sio2})

    else:
        return redirect(reverse('index'))
