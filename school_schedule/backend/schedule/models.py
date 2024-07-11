from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ('Monday', 'Понедельник'),
            ('Tuesday', 'Вторник'),
            ('Wednesday', 'Среда'),
            ('Thursday', 'Четверг'),
            ('Friday', 'Пятница')
        ]
    )
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_name} - {self.subject} - {self.day_of_week} {self.start_time}-{self.end_time}"
