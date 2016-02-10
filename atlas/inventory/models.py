from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Program(models.Model):
    name = models.CharField(max_length=75)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('inventory:program_detail', kwargs={'pk':self.pk})

    def __str__(self, *args, **kwargs):
        return self.name

class Client(models.Model):
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=75)
    is_student = models.BooleanField(default=True)
    year_of_graduation = models.IntegerField(null=True, blank=True)
    program = models.ForeignKey('Program', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('inventory:client_detail', kwargs={'pk':self.pk})

    def __str__(self, *args, **kwargs):
        return self.full_name

class Computer(models.Model):
    serial_number = models.CharField(max_length=12, unique=True)
    model = models.CharField(max_length=40)
    program = models.ForeignKey('Program', on_delete=models.SET_NULL, null=True)
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)

    def __str__(self, *args, **kwargs):
        return self.serial_number
