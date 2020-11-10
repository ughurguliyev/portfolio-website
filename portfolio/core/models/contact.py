from django.db import models 

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name and Surname")
    email = models.EmailField(verbose_name="E-mail")
    message = models.TextField(verbose_name="Message")

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name