# kanban/views.py
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class BulkUpdateTaskView(APIView):
    """
    Update multiple tasks at once.
    """
    def put(self, request, *args, **kwargs):
        response_data = []
        for task_data in request.data:
            task_id = task_data.get('id')
            if task_id:
                # If the task ID is provided, try to get the task.
                try:
                    task = Task.objects.get(id=task_id)
                except Task.DoesNotExist:
                    return Response({'detail': f'Task with id {task_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
                serializer = TaskSerializer(task, data=task_data)
            else:
                # If no task ID is provided, create a new task.
                serializer = TaskSerializer(data=task_data)

            if serializer.is_valid():
                serializer.save()
                response_data.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(response_data, status=status.HTTP_200_OK)