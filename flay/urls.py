from rest_framework import routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from flay.views import HospitalViewsSets, DoctorsViewsets

#Создание маршрута с views
router = DefaultRouter()
router.register("hospital", HospitalViewsSets)
router.register("doctor", DoctorsViewsets)

urlpatterns = [
    path("", include(router.urls)),


]
