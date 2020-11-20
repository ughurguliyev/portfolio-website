from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

from .category import Category


class Project(models.Model):
    title = models.CharField(
        max_length = 100, 
        verbose_name = "Title"
    )
    description = models.TextField(verbose_name="Description")
    pub_date = models.DateTimeField()
    featured_image = models.ImageField(
        null = True, 
        verbose_name = "Image"
    )
    category = models.ForeignKey(
        Category, 
        on_delete = models.CASCADE,
        null = True
    )
    slug = AutoSlugField(populate_from='title', null=True)


    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title