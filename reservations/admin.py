from django.contrib import admin

# Register your models here.
from .models import Reservation, Avis

admin.site.register(Reservation)
admin.site.register(Avis)