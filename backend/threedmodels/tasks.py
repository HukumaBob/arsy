from celery import shared_task
import logging


@shared_task
def process_file(file_id):
    from models import ThreeDModel
    logger = logging.getLogger(__name__)
    logger.info(f"Celery task started for file with ID{file_id}")

    try:
        file = ThreeDModel.objects.get(id=file_id)
        file.processed = True
        file.save()

    except ThreeDModel.DoesNotExist as e:
        logger.error(f"An error has occurred:{e}")


