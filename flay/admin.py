import textwrap

from django.contrib import admin

from flay.models import Hospital, Doctor, Specialization, Department


admin.site.register(Specialization)
admin.site.register(Department)

# Создание кастомный админке

@admin.register(Hospital)
class AdminHospital(admin.ModelAdmin):
    # Отоброженеи в админке
    list_display = (
        "name",
        "class_hospital",
        "time_work_display",
        "address",
        "date",
    )

    # Фильтрция для админке
    list_display_links = ("name", "address")
    list_filter = ("name", "class_hospital")

    # Поиск в админке
    search_fields = ("name", "address")
    def time_work_display(self, obj: Hospital):
        return obj.time_work()
    time_work_display.short_description = "Время работы"

@admin.register(Doctor)
class AdminDoctor(admin.ModelAdmin):
    list_display = (
        "name",
        "firs_name",
        "birthday",
        "specialization",
        "department",
    )

    list_display_links = ("name", "department")
    list_filter = ("firs_name","specialization" )
    search_fields = ("specialization", "department", "name")


