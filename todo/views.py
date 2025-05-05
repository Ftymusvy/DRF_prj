from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET' ,'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
            todos = Todo.objects.order_by('priority').all()
            todo_serializer = TodoSerializer(todos , many=True)
            return Response(todo_serializer.data , status.HTTP_202_ACCEPTED)
    elif request.method == 'POST':
            serializer = TodoSerializer(data = request.data)
            if serializer.is_valid():
                   serializer.save()
                   return Response(serializer.data , status.HTTP_201_CREATED)
    return Response(None , status.HTTP_400_BAD_REQUEST)
