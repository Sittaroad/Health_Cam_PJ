from django.db import models

# Create your models here.
class timer(models.Model):
    name = models.CharField(max_length=255)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name