import django
from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=50, null=False)
    brand = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    filename = models.CharField(max_length=50, null=False)
    user = models.ForeignKey(django.contrib.auth.get_user_model(), on_delete=models.CASCADE)
    #faz com q se o user for apagado, seus registros tbm serão

    def __str__(self):
        return self.model + ' ano: ' + str(self.year) #converte para str