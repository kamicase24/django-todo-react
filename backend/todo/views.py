from django.shortcuts import render

from rest_framework import viewsets
from todo.serializers import ToDoSerializers
from todo.models import ToDo 

class ToDoView(viewsets.ModelViewSet):
    serializer_class = ToDoSerializers
    queryset = ToDo.objects.all()
