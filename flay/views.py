from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from flay.filters import HospitalFilter, DoctorFilter
from flay.models import Hospital, Doctor
from flay.ordering import DoctorOrderingFilter, HospitalOrderingFilter
from flay.search import DoctorSearchFilter, HospitalSearchFilter
from flay.serilizers import HospitalSerializers, SerializersDoctor

# Создание страниц для сайта

class PaginationViews(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 20000

# Полный CRUD
class HospitalViewsSets(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializers
    # permission_classes = (IsAuthenticated,)
    # Пагинцая нужна для огронмчение видемых списков на сайте
    pagination_class = PaginationViews

    # Указываем все фильтры, поиск и сортировку
    filter_backends = (DjangoFilterBackend,HospitalSearchFilter, HospitalOrderingFilter )
    filterset_class = HospitalFilter

class DoctorsViewsets(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = SerializersDoctor
    # Пагинцая нужна для огронмчение видемых списков на сайте
    pagination_class = PaginationViews

    # Указываем все фильтры, поиск и сортировку
    filter_backends = (DjangoFilterBackend,DoctorSearchFilter, DoctorOrderingFilter)
    filterset_class = DoctorFilter
    search_fields = DoctorSearchFilter

