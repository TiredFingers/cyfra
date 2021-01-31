from django.contrib import admin
from .models import Car, OreStore, CarModel


class CarAdmin(admin.ModelAdmin):
    pass


class OreStoreAdmin(admin.ModelAdmin):
    pass


class CarModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Car, CarAdmin)
admin.site.register(OreStore, OreStoreAdmin)
admin.site.register(CarModel, CarModelAdmin)
