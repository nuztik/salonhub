from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


#список услуг салона
class SalonList(ListView):
    pass

#список мастеров салона
class MasterList(ListView):
    pass

#список услуг определенного мастера
class MasterDetail(DetailView):
    pass

#подробное описание услуги
class ServiceDetail(DetailView):
    pass

#создание услуги мастером
class ServiceCreate(CreateView):
    pass

#изменение услуги мастером
class ServiceUpdate(UpdateView):
    pass

#удаление услуги мастером
class ServiceDelete(DeleteView):
    pass

#поиск услуги
class SearchServiceList(ListView):
    pass

#список клиентов определенного мастера
class ClientList(ListView):
    pass

#список услуг на которые ходил клиент
class ClientDetail(ListView):
    pass

# функция записи на услугу
@login_required
def sign_up(request, pk):
    pass

#функция удалить запись
@login_required
def del_entry(request, pk):
    pass




