from django.db import models

class Image(models.Model):
    
    title = models.CharField('', max_length=50)
    picture = models.ImageField('', upload_to='images/')
    text = models.TextField('', max_length=1000, blank=True)

    def __str__(self):
        return self.title