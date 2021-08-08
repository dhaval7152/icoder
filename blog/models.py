from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    image=models.ImageField(upload_to="blog/images")
    content=models.TextField()

    def __str__(self):
        return self.title + " by " + self.author

