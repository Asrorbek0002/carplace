from django.urls import path

from cars.views import contact_form_handler, index, search_car_handler

app_name = "cars"

urlpatterns = [
    path("index/", index, name="index"),
    path("contactmessage/", contact_form_handler, name="contactmessage"),
    path("search/", search_car_handler, name="search-car"),
]
