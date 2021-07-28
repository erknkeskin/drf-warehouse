from django.db import models


class Box(models.Model):
    class Meta:
        verbose_name_plural = 'Boxes'

    name = models.CharField(max_length=120, verbose_name='Box Name', null=False)
    volume = models.IntegerField(verbose_name='Volume', null=False)
    created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name
