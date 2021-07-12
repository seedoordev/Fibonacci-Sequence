from collections import OrderedDict

from rest_framework import serializers

from .models import FibonacciSequence, ResultNumber


class FibonacciPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FibonacciSequence
        fields = ("parameter",)

    def validate(self, data):
        if data["parameter"] < 0:
            raise serializers.ValidationError(
                "Параметр - положительное число"
            )
        return data


class FibonacciListSerializer(serializers.ModelSerializer):
    operation_time = serializers.SerializerMethodField('get_operation_time')

    def get_operation_time(self, instance):
        if instance.end_datetime:
            return instance.end_datetime - instance.start_datetime

    class Meta:
        model = FibonacciSequence
        fields = "__all__"

    def to_representation(self, instance):
        result = super(FibonacciListSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key]])


class ResultNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultNumber
        fields = ("number",)

    def to_representation(self, instance):
        result = super(ResultNumberSerializer, self).to_representation(instance)
        for key in result:
            number = int(result[key])
        return number


class FibonacciRetrieveSerializer(serializers.ModelSerializer):
    operation_time = serializers.SerializerMethodField('get_operation_time')
    sequence = ResultNumberSerializer(many=True, read_only=True)

    def get_operation_time(self, instance):
        if instance.end_datetime:
            return instance.end_datetime - instance.start_datetime

    class Meta:
        model = FibonacciSequence
        fields = "__all__"
