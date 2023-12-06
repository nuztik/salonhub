from django.contrib import admin


from .models import Master, Schedule, Service, Client, Salon

# добавление специальной модели в admin панель
class ScheduleInline(admin.StackedInline):
    model = Schedule
    extra = 0

class MasterAdmin(admin.ModelAdmin):
    inlines = [
        ScheduleInline,
    ]

admin.site.register(Master, MasterAdmin)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Salon)
# Register your models here.
