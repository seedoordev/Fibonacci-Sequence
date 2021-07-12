from django.urls import path

from .views import FibonacciSequenceView, FibonacciNumberView

urlpatterns = [
    # path("numbers/", FibonacciNumberViewSet.as_view({"get": "list", "post": "create"})),
    # path("numbers/<int:pk>/", FibonacciNumberViewSet.as_view({"get": "retrieve",})),
    path("numbers/", FibonacciSequenceView.as_view()),
    path("numbers/<int:pk>/", FibonacciNumberView.as_view({"get": "retrieve",})),
]