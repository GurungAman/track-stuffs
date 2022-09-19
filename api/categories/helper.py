from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=128)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ('-added_at',) # - represents descending
        
    def __str__(self):
        return self.name

