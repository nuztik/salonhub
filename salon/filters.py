import django_filters.widgets
from django_filters import FilterSet, CharFilter, DateFromToRangeFilter
from django_filters.widgets import DateRangeWidget

from .models import Service


#построение фильтров поиска
class ServiceFilter(FilterSet):
    master = CharFilter(
        field_name='master__user__username',
        lookup_expr='icontains',
        label='Мастер'
    )

    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Услуга'
    )

    class Meta:
        model = Service
        fields = {'title'}