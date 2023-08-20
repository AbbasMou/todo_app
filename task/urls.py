from django.urls import path

from .views import (TaskListView,
                    TaskCreateView,
                    TaskDetailView,
                    TaskDeleteView,
                    TaskUpdateView)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-home'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task-delete'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task-home-delete'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task-update'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='task-home-update'),

]
