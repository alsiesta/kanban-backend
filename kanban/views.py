# kanban/views.py
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .permissions import IsSuperUserOrReadOnly
from django.contrib.auth import get_user_model, logout




from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth import get_user_model

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_type': 'superuser' if user.is_superuser else 'normaluser',
        })

class LogoutView(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TaskListCreateView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    # authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]

class UserListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserCreateView(APIView):
    def post(self, request):
        User = get_user_model()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
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