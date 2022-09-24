from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    alt_phone = models.CharField(max_length=10)
    email = models.EmailField()
    society = models.CharField(max_length=70)
    house_no = models.CharField(max_length=10)
    pin_code = models.CharField(max_length=10)
    landmark = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    weight = models.CharField(max_length=10)
    date_time = models.DateField()




