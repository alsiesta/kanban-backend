from django.contrib import admin
from django.urls import path
from home.views import HomeContentView
from posts.views import PostItemView, PostItemUpdateView
from kanban.views import TaskListCreateView, TaskDetailView, BulkUpdateTaskView, UserListView, LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('posts/', PostItemView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostItemUpdateView.as_view(), name='post-update'),
    path('contents/', HomeContentView.as_view(), name='contents'),
    path('contents/image/<str:image_name>/', HomeContentView.as_view(), name='contents_image'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/bulk_update/', BulkUpdateTaskView.as_view(), name='task-bulk-update'),
    path('users/', UserListView.as_view(), name='user-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
