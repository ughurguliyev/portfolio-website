from django.db import models

from .category import Category


class Article(models.Model):
    title = models.CharField(max_length=60, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    pub_date = models.DateTimeField()
    featured_image = models.ImageField(verbose_name="Post image", null=True)

    like_count = models.IntegerField(default=0 ,verbose_name="Like count")
    view_count = models.IntegerField(default=0, verbose_name="View count")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)


    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title