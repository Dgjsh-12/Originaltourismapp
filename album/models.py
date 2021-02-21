from django.db import models

class Image(models.Model):
    
    title = models.CharField('タイトル', max_length=50)
    picture = models.ImageField('画像', upload_to='images/')
    text = models.TextField('内容', max_length=1000, blank=True)

    def __str__(self):
        return self.title