from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



# No longer need these approaches. Left as notes

# class TodoList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class CurrentTask(generics.RetrieveDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# class UpdateTask(generics.UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     http_method_names = ['put']