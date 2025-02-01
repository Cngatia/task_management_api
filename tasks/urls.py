from django.urls import path, include
from .views import TaskListCreateView, TaskDetailView, TaskCompleteToggleView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', TaskCompleteToggleView.as_view(), name='task-complete-toggle'),
    path('tasks'),
]
