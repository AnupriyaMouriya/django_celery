import celery
from celery import result
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Tasks
from .serializers import TasksSerializer, TasksListSerializer

from tutorial import task_wait

@api_view(['GET', 'POST'])
def task_list(request ,format=None):

    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksListSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            x=task_wait.delay()
            print (type(x))
            serializer.validated_data["task_celery"]=x
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail(request, id, format=None):

    try:
        task = Tasks.objects.get(id=id)
        p=task.task_celery
        p=celery.result.AsyncResult(p)
        task.status=p.state
        if task.status=='SUCCESS':
            task.output="COMPLETED"
        task.save()
        print (task.status)
    except Tasks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TasksListSerializer(task)
        print (serializer.data)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)