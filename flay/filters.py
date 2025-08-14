from django_filters import rest_framework as filters, CharFilter

from flay.models import Hospital, Doctor

# Необходимый класс для создание Фильтраций

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


# Обект по которым будет фильтрация
class HospitalFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name="name", lookup_expr="in")
    class_hospital = CharFilterInFilter(field_name="class_hospital", lookup_expr="in")
    doctor_name = CharFilterInFilter(field_name="doctors__name", lookup_expr="in")
    department_name = CharFilterInFilter(field_name="department_name", lookup_expr="in")




    class Meta:
        model = Hospital
        fields = ["name", "class_hospital", "doctor_name", "department_name"]


class DoctorFilter(filters.FilterSet):
    name = CharFilterInFilter(field_name="name", lookup_expr="in")
    specialization = CharFilterInFilter(field_name="specialization__name", lookup_expr="in")
    department = CharFilterInFilter(field_name="department__name", lookup_expr="in")
    birthday_after = filters.DateFilter(field_name="birthday", lookup_expr="gte")
    birthday_before = filters.DateFilter(field_name="birthday", lookup_expr="lte")

    class Meta:
        model = Doctor
        fields = ["name", "specialization", "department", "birthday_after", "birthday_before"]


