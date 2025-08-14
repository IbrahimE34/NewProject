from django.db import models
#  Создание модели для департамента
class Department(models.Model):
    name = models.TextField(verbose_name="Укожите Отделение", blank=False, null=False)

# Для боле красивого вида в админке

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"


# Созданеи специальности

class Specialization(models.Model):
    name = models.TextField(verbose_name="Укожите специальность", blank=False, null=False)
    descriptions = models.TextField(blank= True,null =  False)

# Для боле красивого вида в админке

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Спецалсит"
        verbose_name_plural = "Спецалситы"


# Создание докторов

class Doctor(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    firs_name = models.CharField(max_length=40)
    birthday = models.DateField()
    specialization = models.ForeignKey(Specialization,on_delete= models.PROTECT, db_index=True)
    department = models.ForeignKey(Department, on_delete= models.PROTECT, db_index=True)

    # Для боле красивого вида в админке
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Доктор"
        verbose_name_plural = "Доктора"


# Создание Госпиталя
class Hospital(models.Model):
    name = models.CharField(max_length=30, db_index=True)
    class_hospital = models.CharField(max_length=50)
    address = models.TextField(db_index=True)
    open_time = models.TimeField("Время открытия", blank=True, null=True)
    close_time = models.TimeField("Время закрытия", blank=True, null=True)
    date = models.DateField()
    doctors = models.ManyToManyField("Doctor")

# Функция для роботы с времинем
    def time_work(self):
        if self.open_time and self.close_time:
            return f"{self.open_time.strftime('%H:%M')} – {self.close_time.strftime('%H:%M')}"
        return "Время не указано"

# Для боле красивого вида в админке
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Госпиталь"
        verbose_name_plural = "Госпитали"

