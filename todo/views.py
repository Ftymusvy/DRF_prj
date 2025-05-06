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


@api_view(['GET' ,'PUT' , 'DELETE'])
def todo_detail_view(request: Request , todo_id:int):
    try:
           
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response(None , status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
          serializer = TodoSerializer(todo)
          return Response(serializer.data , status.HTTP_200_OK)

    elif request.method == 'PUT':
          serializer = TodoSerializer(todo , data=request.data)
          if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status.HTTP_202_ACCEPTED)
          return Response(serializer.data , status.HTTP_400_BAD_REQUEST)

    elif  request.method == 'DELETE':
           todo.delete()
           return Response(None, status.HTTP_204_NO_CONTENT)
           