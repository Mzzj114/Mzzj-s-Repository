from django.db import models

# Create your models here.


class chatRecord(models.Model):
    texts = models.TextField()
    post_date = models.DateTimeField()
    filename = models.CharField(max_length=50, default='')
    upload = models.FileField(upload_to="upload/", default='')

    def __str__(self):
        return self.texts+" "+self.upload.name


