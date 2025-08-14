from rest_framework import filters

class HospitalOrderingFilter(filters.OrderingFilter):
    ordering_param = "sort"
    default_ordering_fields = [
        "name",
        "class_hospital",
        "doctors__name",
        "doctors__department__name"
    ]

    def get_ordering_fields(self, view, request):
        return getattr(view, "ordering_fields", self.default_ordering_fields)


class DoctorOrderingFilter(filters.OrderingFilter):
    ordering_param = "sort"
    default_ordering_fields = [
        "name",
        "specialization__name",
        "department__name",
        "birthday"
    ]

    def get_ordering_fields(self, view, request):
        return getattr(view, "ordering_fields", self.default_ordering_fields)
