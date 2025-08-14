from rest_framework import filters
from rest_framework import filters

class HospitalSearchFilter(filters.SearchFilter):
    search_param = "q"
    default_search_fields = [
        "name",
        "class_hospital",
        "doctors__name",
        "doctors__department__name"
    ]

    def get_search_fields(self, view, request):
        return getattr(view, "search_fields", self.default_search_fields)


class DoctorSearchFilter(filters.SearchFilter):
    search_param = "q"
    default_search_fields = [
        "name",
        "specialization__name",
        "department__name"
    ]

    def get_search_fields(self, view, request):
        return getattr(view, "search_fields", self.default_search_fields)

