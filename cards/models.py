from django.db import models


class CardTaro(models.Model):
    name = models.CharField(max_length=255)
    description_meaning = models.TextField()
    description_advance = models.TextField()
    image = models.CharField(max_length=255)

    def str(self):
        return self.name
