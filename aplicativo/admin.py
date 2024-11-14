from django.contrib import admin

from aplicativo.models import Car

class CarFilter(admin.ModelAdmin):
    list_display = ("id", "model", "brand", "year") 
    #nome dos campos dos modelos que estavam nas linhas
    list_display_links = ("id", "model", "brand", "year")
    list_filter = ("model", "year")
    search_fields = ("year", "model", "brand")

admin.site.register(Car, CarFilter)