from rest_framework import routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from flay.views import HospitalViewsSets, DoctorsViewsets, ViewsPatient

#Создание маршрута с views
router = DefaultRouter()
router.register("hospital", HospitalViewsSets)
router.register("doctor", DoctorsViewsets)
router.register("patient", ViewsPatient)

urlpatterns = [
    path("", include(router.urls)),


]
