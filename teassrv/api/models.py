from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tea(models.Model):
    name = models.CharField(max_length=225)
    # MI adta meg a valaszt, hogy ezt igy kell
    brand_id = models.ForeignKey(Brand, related_name='teas', on_delete=models.CASCADE)
    range = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    qty = models.IntegerField()
    unit = models.CharField(max_length=255)
    price = models.IntegerField()


    def __str__(self):
        return f"{self.brand_id} ----- {self.name}"
