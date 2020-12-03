import os

from django.db import models


class CourseModel(models.Model):
    class Meta:
        db_table = 'course'
        verbose_name = 'курс'
        verbose_name_plural = 'курси'

    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=os.path.join('course', 'img'), default='', blank=True)
    price = models.IntegerField()
    description = models.CharField(max_length=500, default='', blank=True)
    date_beginnings = models.DateField()
    date_endings = models.DateField()

    def __str__(self):
        return self.name
