from django.contrib import admin

from aplicativo.models import Car

class CarFilter(admin.ModelAdmin):
    list_display = ("id","user", "model", "brand", "year") 
    #nome dos campos dos modelos que estavam nas linhas
    list_display_links = ("id", "model", "brand", "year") #tranforma em links
    list_filter = ("model", "year") #filtra
    search_fields = ("year", "model", "brand") #cria a caixa de pesquisa

admin.site.register(Car, CarFilter) #tem q ser registrado o filter para funcionar