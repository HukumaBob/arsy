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
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

            # Получите объект файла, который был только что сохранен
            file = file_serializer.instance

            # Запустите задачу Celery для обработки файла
            task = process_file.delay(file.id)

            # Периодически проверяйте статус задачи
            while not task.ready():
                pass

            if task.successful():
                # Если задача успешно выполнена, обновите данные в сериализаторе
                file.refresh_from_db()
                updated_serializer = FileSerializer(file)
                return Response(updated_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("File processing failed", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
