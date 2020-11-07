from django.db import models

from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    pub_date = models.DateTimeField()
    featured_image = models.ImageField(null=True, verbose_name="Image")


    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title