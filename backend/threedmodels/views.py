from celery.result import AsyncResult
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ThreeDModel
from api.serializers import FileSerializer
from .tasks import process_file
from api.pagination import CustomPagination


class FileUploadView(APIView):
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            file = file_serializer.instance
            task = process_file.delay(file.id)
            return Response({'task_id': task.id}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatusView(APIView):
    def get(self, request, task_id):
        task = AsyncResult(task_id)
        return Response({'status': task.status, 'result': task.result})


class FileListView(ListAPIView):
    queryset = ThreeDModel.objects.all()
    serializer_class = FileSerializer
    pagination_class = CustomPagination
