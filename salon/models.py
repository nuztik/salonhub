from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Schedule(models.Model):
    pass


class Master(models.Model):
    names = models.OneToOneField(User, on_delete=models.CASCADE)
    # date = models.DateTimeField(u'Дата и время', default=timezone.now)
    schedules = models.OneToOneField(Schedule, on_delete=models.CASCADE)



class Service(models.Model):
    pass


class Client(models.Model):
    pass


class Salon(models.Model):

    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150, default='не указан')
    contact = models.CharField(max_length=12, default='не указан')
    masters = models.ForeignKey(Master, on_delete=models.CASCADE)
    servies = models.ForeignKey(Service, on_delete=models.CASCADE)
    scheule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    # date = models.DateTimeField(u'Дата и время',default=timezone.now)







