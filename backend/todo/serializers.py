from rest_framework import serializers
from todo.models import ToDo

class ToDoSerializers(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = ('id', 'title', 'description', 'completed')