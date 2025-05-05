from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todofields = ['id' , 'title' , 'content']