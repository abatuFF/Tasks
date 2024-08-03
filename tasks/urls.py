from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, index

urlpatterns = [
    path('', index, name='index'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),
]
