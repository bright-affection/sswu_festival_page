from django.db import models

class Info(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title