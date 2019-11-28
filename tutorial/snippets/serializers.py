from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only=  True)
    #task_name = serializers.CharField(required=True)
    class Meta:
        model = Tasks
        fields = ['id', 'task_name' , 'status','output','task_celery']

class TasksListSerializer(serializers.ModelSerializer):
    #id = serializers.IntegerField(read_only=  True)
    #task_name = serializers.CharField(required=True)
    class Meta:
        model = Tasks
        fields = ['id', 'task_name' , 'status','output']

