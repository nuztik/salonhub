from django.urls import path

from .views import SalonList, SalonDetail, MasterList, MasterDetail, ServiceDetail, ServiceCreate, \
    ServiceUpdate, ServiceDelete, SearchServiceList, ClientList, ClientDetail, sign_up, del_entry

urlpatterns = [
    path('salons/',SalonList.as_view(), name='salons'),
    path('salon/<int:pk>/', SalonDetail.as_view(), name='salon'),
    path('masters/', MasterList.as_view(), name='masters'),
    path('masters/<int:pk>/', MasterDetail.as_view(), name='master'),
    path('service/<int:pk>/', ServiceDetail.as_view(), name='service'),
    path('service/create/', ServiceCreate.as_view(), name='s_create'),
    path('service/<int:pk>/update/', ServiceUpdate.as_view(), name='s_update'),
    path('service/<int:pk>/delete/', ServiceDelete.as_view(), name='s_delete'),
    path('service/search/', SearchServiceList.as_view(), name='s_search'),
    path('clients/', ClientList.as_view(), name='clients'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client'),
    path('service/<int:pk>/sign_up/', sign_up, name='sign_up'),
    path('service/<int:pk>/del_entry', del_entry, name='del_entry')

]