from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='todo'),
    path('task/<int:pk>/', views.CurrentTask.as_view(), name='current-task')
]