from django.db import models
from django.utils import timezone


class Building(models.Model):
    title = models.CharField(max_length=200)
    building_address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    establishment_date = models.DateTimeField(blank=True, null=True)

    def get_bricks_amount(self):
        bricks_amount = sum(list(Task.objects.filter(
            building_number=self.id
        ).values_list('bricks_quantity', flat=True)))
        return bricks_amount

    def establish(self):
        self.establishment_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'


class Task(models.Model):
    building_number = models.ForeignKey(
        'Building',
        on_delete=models.CASCADE
    )
    bricks_quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
