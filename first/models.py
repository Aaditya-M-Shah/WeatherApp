from django.db import models


class City(models.Model):
    name=models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Cities"
    
# after making models you always have to migrate 