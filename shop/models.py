from django.db import models

class Test(models.Model):
    name = models.CharField(verbose_name='имя', max_length=150)
    tel = models.CharField(verbose_name='телефон', max_length=150)

    def __str__(self):
        return self.name
