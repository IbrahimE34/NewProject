from rest_framework import serializers

from flay.models import Hospital, Doctor, Specialization, Department

# Общеие создание сериализаций для json в хроме
class SpecializationSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()
    class Meta:
        model = Specialization
        fields = ["id", "name", "short_description"]

    # Функция для огроничение видемости слов в json
    def get_short_description(self, obj):
        return obj.descriptions[:15] + "..." if len(obj.descriptions) > 50 else obj.descriptions


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name"]


class SerializersDoctor(serializers.ModelSerializer):
    specialization = serializers.StringRelatedField()
    department = serializers.StringRelatedField()

    class Meta:
        model = Doctor
        fields = (
            "name",
            "firs_name",
            "specialization",
            "department",
        )

class HospitalSerializers(serializers.ModelSerializer):
    doctors = SerializersDoctor(many=True)

    class Meta:
        model = Hospital
        fields = (
            "id",
            'name',
            'address',
            'class_hospital',
            'time_work',
            "date",
            "doctors",
        )


