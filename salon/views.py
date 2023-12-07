from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from public.salon.filters import ServiceFilter
from public.salon.forms import ServiceForm
from public.salon.models import Service, Master, Client


#список услуг салона
class SalonList(ListView):
    model = Service
    ordering = 'title'
    template_name = 'salon.html'
    context_object_name = 'salon'
    paginate_by = 10


#список мастеров салона
class MasterList(ListView):
    model = Master
    ordering = 'title'
    template_name = 'masters.html'
    context_object_name = 'masters'
    paginate_by = 10

#список услуг определенного мастера
class MasterDetail(DetailView):
    model = Service
    ordering = 'title'
    template_name = 'master.html'
    context_object_name = 'master'
    paginate_by = 10

#подробное описание услуги
class ServiceDetail(DetailView):
    model = Service
    ordering = 'title'
    template_name = 'service.html'
    context_object_name = 'masters'
    paginate_by = 10

#создание услуги мастером
class ServiceCreate(CreateView):
    form_class = ServiceForm
    model = Service
    template_name = 'service_create.html'

    # может создать/сохранить только мастер
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_master'] = not self.request.user.groups.filter(name='master').exists()
        return context

    # функция добавления в таблицу услуг
    def form_valid(self, form):
        service = form.save(commit=False)
        service.service_master = self.request.user
        service.save()
        return super().form_valid(form)

#изменение услуги мастером
class ServiceUpdate(UpdateView):
    form_class = ServiceForm
    model = Service
    template_name = 'service_create.html'
    success_url = reverse_lazy('service')

    # функция изменения в таблице услуг
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_master'] = not self.request.user.groups.filter(name='master').exists()
        return context

#удаление услуги мастером
class ServiceDelete(DeleteView):
    model = Service
    template_name = 'service_del.html'

#поиск услуги
class SearchServiceList(ListView):
    model = Service
    ordering = 'title'
    template_name = 'service_search.html'
    context_object_name = 'service_search'

    # функции фильтрации по заданному поиску
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ServiceFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


#список клиентов определенного мастера
class ClientList(ListView):
    model = Client
    ordering = 'title'
    template_name = 'clients.html'
    context_object_name = 'clients'
    paginate_by = 10

    #сортировка клиентов по мастеру
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_to_master = Client.objects.filter(master=self.request.user)
        context['client_to_master'] = client_to_master
        return context


#список услуг на которые ходил клиент
class ClientDetail(ListView):
    model = Service
    ordering = 'title'
    template_name = 'client.html'
    context_object_name = 'client'
    paginate_by = 10

    #сортировка услуг по заданному клиенту
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_to_service = Service.objects.filter(client=self.request.user)
        context['client_to_service'] = client_to_service
        return context

# функция записи на услугу
@login_required
def sign_up(request, pk):
    user = request.user
    service = Service.objects.get(id=pk)
    service.record = True
    service.save(user)
    message = 'Вы записаны'
    return render(request, 'sign_up.html', {'service': service, 'message': message})

#функция удалить запись
@login_required
def del_entry(request, pk):
    user = request.user
    service = Service.objects.get(id=pk)
    service.record = False
    service.save(user)
    message = 'Вы отменили запись'
    return render(request, 'del_entry.html', {'service': service, 'message': message})




