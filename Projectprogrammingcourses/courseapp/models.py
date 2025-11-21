from django.db import models

class Teachers(models.Model):
    name = models.CharField("Имя", max_length=50, default="")
    surname = models.CharField("Фамилия", max_length=50, default="")
    surname2 = models.CharField("Отчество", max_length=50, default="")
    birthday = models.DateField("Дата рождения")
    gender = models.CharField("Пол")
    phone_number = models.CharField("Номер телефона", max_length=11)
    
    def __str__(self):
        return f"{self.surname}"
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ["surname","name", "surname2"]      
    

    
class Practice(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    date = models.DateField("Дата")
    assessment = models.IntegerField("Оценка")
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Учебная Практика"
        verbose_name_plural = "Учебная Практика"
    
class Group(models.Model):
    name = models.CharField("Название", max_length=50, unique=True)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    practice = models.ManyToManyField(Practice)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

class Students(models.Model):
    name = models.CharField("Имя", max_length=50, default="")
    surname = models.CharField("Фамилия", max_length=50, default="")
    surname2 = models.CharField("Отчество", max_length=50, default="")
    birthday = models.DateField("Дата рождения")
    gender = models.CharField("Пол")
    phone_number = models.CharField("Номер телефона", max_length=11)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"{self.surname}"
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["surname","name", "surname2"]
    
class Journal(models.Model):
    student = models.ForeignKey(Group, related_name='+', on_delete=models.CASCADE)
    course = models.ForeignKey(Group, related_name='+',on_delete=models.CASCADE)
    date = models.DateField("Дата")
    assessment = models.IntegerField("Оценка")
    def __str__(self):
        return f"{self.date}"
    class Meta:
        verbose_name = "Журнал"
        verbose_name_plural = "Журнал"
    
class Courses(models.Model):
    name = models.CharField("Название", max_length=100, unique=True)
    group = models.ManyToManyField(Group)
    teachers = models.ManyToManyField(Teachers)
    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"