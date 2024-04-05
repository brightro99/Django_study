from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo, Solution
from .serializers import TodoSerializer, SolutionSerializer


# Create your views here.
class TodoView(
    viewsets.ModelViewSet
):  # Query를 통해 데이터를 가져오고 Serializer를 통해 뿌려준다.
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class SolutionView(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
