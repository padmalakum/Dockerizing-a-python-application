from django.db import models


# Create your models here.
class assessment(models.Model):
    text = models.CharField(max_length=500, blank=False, null=False)
    start = models.IntegerField()
    end = models.IntegerField()

    def __str__(self):
        return "{}".format(self.text)
