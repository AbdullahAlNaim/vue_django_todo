from django.urls import path, include
from . import views
from .views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls), name='todo'),


    # dont need these urls. Left as notes
    # path('task/<int:pk>/', views.CurrentTask.as_view(), name='current-task'),
    # path('task/<int:pk>/edit', views.UpdateTask.as_view(), name='edit-task')
]