from rest_framework import serializers  # api를 통해 보내기 위해
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("id", "title", "completed")
