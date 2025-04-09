from django.db import models


class SiteUser(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name='ФИО'
    )

    email = models.EmailField(
        max_length=50,
        verbose_name='Email'
    )

    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )

    def __str__(self):
        return f"{self.full_name}"
