from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Service(models.Model):
    title = models.CharField(max_length=50, default='не указана')
    price = models.FloatField()
    times = models.CharField(max_length=5, default=30)

    def __str__(self):
        return f'{self.title}: {self.price}: {self.times}'


class Master(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    # date = models.DateTimeField(u'Дата и время', default=timezone.now)
    # schedules = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    position = models.CharField(max_length=50, default='не указана')
    description = models.TextField( default='не указанo')
    service = models.ForeignKey( Service, on_delete=models.CASCADE)
    is_active = models.BooleanField( default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    date = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return f'{self.name}: {self.position}: {self.description}: {self.service}'


class Schedule(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    date = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return f'{self.master}: {self.date}'


class Client(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.contact}: {self.service}'


class Salon(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150, default='не указан')
    contact = models.CharField(max_length=12, default='не указан')
    masters = models.ForeignKey(Master, on_delete=models.CASCADE)
    servies = models.ForeignKey(Service, on_delete=models.CASCADE)
    scheule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    # date = models.DateTimeField(u'Дата и время',default=timezone.now)

    def __str__(self):
        return f'{self.title}: {self.address}: {self.contact}:'







