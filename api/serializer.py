from rest_framework import serializers
from reminder.models import Task

class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields="__all__"