from django.db import models
from django.utils import timezone as tz


class FibonacciSequence(models.Model):
    STATUS_TYPE_CHOICES = [
        ('OK', 'Done'),
        ('IP', 'In progress'),
    ]
    parameter = models.IntegerField(primary_key=True)
    start_datetime = models.DateTimeField(default=tz.now)
    end_datetime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=2, choices=STATUS_TYPE_CHOICES, default="IP"
    )


class ResultNumber(models.Model):
    sequence_parameter = models.ForeignKey("FibonacciSequence", on_delete=models.CASCADE, related_name="sequence")
    number = models.CharField(max_length=10000, null=True, blank=True)
