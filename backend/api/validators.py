from django.conf import settings
from rest_framework import serializers
from django.core.files.uploadedfile import UploadedFile


def check_file_size(file: UploadedFile):
    if file.size > settings.MAX_FILE_SIZE:
        raise serializers.ValidationError(f'File too large. Size should not exceed {settings.MAX_FILE_SIZE} GB.')