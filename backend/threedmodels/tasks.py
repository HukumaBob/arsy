from celery import shared_task
import logging
from .models import ThreeDModel


@shared_task
def process_file(file_id):
    print('111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    logger = logging.getLogger(__name__)
    logger.info(f"Celery task started for file with ID{file_id}")

    try:
        file = ThreeDModel.objects.get(id=file_id)
        process_file_contents(file)  # Здесь вероятно и будет конвертация файла
        file.processed = True
        file.save()

    except ThreeDModel.DoesNotExist as e:
        logger.error(f"An error has occurred:{e}")


# Функция для обработки содержимого файла
def process_file_contents(file):
    # Просто замените этот комментарий на ваш реальный код обработки файла
    pass
