from .models import Task, User
from .serializers import TaskSerializer, UserSerializer
from rest_framework import viewsets


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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