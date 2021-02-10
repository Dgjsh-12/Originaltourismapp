from django.db import models

class Image(models.Model):
    picture = models.ImageField(upload_to='images/')
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('内容', max_length=1000)

    def __str__(self):
        return self.title