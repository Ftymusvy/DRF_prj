from django.shortcuts import render 
from todo.models import Todo
from django.http import HttpRequest , JsonResponse
from rest_framework.request import Request

def index_page(request):
    context = {
        'todos': Todo.objects.order_by('priority').all()
    }
    return render(request , 'home/index.html' , context)


def todos_json(request : HttpRequest):
    
    todos = list(Todo.objects.order_by('priority').all().values('title' ,'is_done'))
    return JsonResponse({'todos': todos})
