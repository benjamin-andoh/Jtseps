from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dated_registered = models.DateTimeField(auto_created=True)

    def get_absolute_url(self):
        return reverse('customer-list', kwargs={'id': self.id})


class Next_of_kin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
