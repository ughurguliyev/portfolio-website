from django.db import models
from autoslug import AutoSlugField

from .category import Category


class Article(models.Model):
    title = models.CharField(max_length=60, verbose_name="Title", unique=True)
    description = models.TextField(verbose_name="Description")
    pub_date = models.DateTimeField()
    featured_image = models.ImageField(verbose_name="Post image", null=True)
    slug = AutoSlugField(populate_from='title', null=True)
    featured_post = models.BooleanField(verbose_name="Highlited post", default=False)

    like_count = models.IntegerField(default=0 ,verbose_name="Like count")
    view_count = models.IntegerField(default=0, verbose_name="View count")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)


    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    

    def __str__(self):
        return self.title