from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserListView
from threedmodels.views import FileUploadView, FileListView, TaskStatusView

app_name = 'api'
router = DefaultRouter()
# router.register(r'users', UserListView)
urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserListView.as_view(), name='users_list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('task-status/<str:task_id>/', TaskStatusView.as_view(), name='task-status'),
]
