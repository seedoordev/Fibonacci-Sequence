from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView

from .serializers import FibonacciPostSerializer, FibonacciListSerializer, FibonacciRetrieveSerializer
from .models import FibonacciSequence
from .tasks import create_fibonacci_siquence


class FibonacciSequenceView(APIView):
    def get(self, request, format=None):
        sequence = FibonacciSequence.objects.all()
        serializer = FibonacciListSerializer(sequence, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FibonacciPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            create_fibonacci_siquence(int(request.data['parameter']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FibonacciNumberView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = FibonacciSequence.objects.all()
    serializer_class = FibonacciRetrieveSerializer
