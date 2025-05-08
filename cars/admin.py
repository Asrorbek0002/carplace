from django.contrib import admin

from cars.models import Brand, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "year", "color", "gear_type", "distance_covered")
    list_filter = ("brand", "gear_type")
    search_fields = ("name", "description")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")
    search_fields = ("name", "description")
