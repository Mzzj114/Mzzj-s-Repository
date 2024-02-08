from django.db import models


# Create your models here.
class postThing(models.Model):
    title = models.CharField(max_length=50, default="default title")
    intro = models.CharField(max_length=150, default="this a brief introduction")
    post_date = models.DateTimeField()

    # text: the path to the blog, ignore the variable's name
    text = models.TextField()



    def __str__(self):
        return self.title
