from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name="Name"
    )


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name
    