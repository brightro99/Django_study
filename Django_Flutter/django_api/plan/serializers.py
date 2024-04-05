from rest_framework import serializers  # api를 통해 보내기 위해
from .models import Todo, Solution


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            "id",
            "title",
            "completed",
        )


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        # fields = "__all__"
        fields = (
            "id",
            "solution",
        )
