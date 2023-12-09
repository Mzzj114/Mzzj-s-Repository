from django.db import models

# Create your models here.


class textPart(models.Model):
    text_name = models.CharField(max_length=100, default="")
    texts = models.CharField(max_length=500, default="")
    texts_en = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.text_name
