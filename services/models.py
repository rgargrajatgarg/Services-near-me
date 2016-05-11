from django.db import models
from django.utils import timezone


class ServiceMen(models.Model):
    author = models.ForeignKey('auth.User')
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    work = models.CharField(max_length=200)
    description = models.TextField()
    distance = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.IntegerField
    joined_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

   # def __str__(self):
     #   return self.title