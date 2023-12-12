from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Master(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    # date = models.DateTimeField(u'Дата и время', default=timezone.now)
    position = models.CharField(max_length=50, default='не указана')
    description = models.TextField( default='не указанo')
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    is_active = models.BooleanField( default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    date = models.DateTimeField( default=timezone.now)
    def __str__(self):
        return f'{self.name}: {self.position}: {self.description}: {self.service}'


class Clients(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12)
    client_time = models.TimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return f'{self.name}: {self.contact}: {self.service}'


class Service(models.Model):
    title = models.CharField(max_length=50, default='не указана')
    master = models.ManyToManyField(Master)
    content = models.CharField(max_length=200,default='не указанo')
    price = models.FloatField()
    times = models.CharField(max_length=3, default=30)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    record = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.title}: {self.price}: {self.times}: {self.master}: {self.content}'


class Schedules(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    date = models.DateTimeField( default=timezone.now)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.master}: {self.date}'


class Salon(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=150, default='не указан')
    contact = models.CharField(max_length=12, default='не указан')
    content = models.CharField(max_length=200, default='не указанo')
    masters = models.ForeignKey(Master, on_delete=models.CASCADE)
    servies = models.ForeignKey(Service, on_delete=models.CASCADE)
    scheule = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Clients)
    # date = models.DateTimeField(u'Дата и время',default=timezone.now)
    def __str__(self):
        return f'{self.title}: {self.address}: {self.contact}: {self.servies}:'







