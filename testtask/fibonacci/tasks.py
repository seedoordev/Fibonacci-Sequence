from celery import shared_task
from django.utils import timezone as tz

from .models import FibonacciSequence, ResultNumber
from .generator import fibonacci


@shared_task
def create_fibonacci_siquence(n):
    sequence = fibonacci(n)
    for number in sequence:
        new_fibonacci_number = ResultNumber.objects.create(number=number, sequence_parameter_id=n)

    final_sequence = FibonacciSequence.objects.get(parameter=n)
    final_sequence.end_datetime = tz.now()
    final_sequence.status = 'OK'
    final_sequence.save()