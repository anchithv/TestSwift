from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
