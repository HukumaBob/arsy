from django.contrib.auth.models import User
from rest_framework import serializers

from threedmodels.models import ThreeDModel

from .validators import check_file_size


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name',
            'last_name', 'email', 'date_joined',
        )
        ref_name = 'ApiUser'


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(
        allow_empty_file=False,
        required=True,
        validators=[check_file_size]
    )

    class Meta:
        model = ThreeDModel
        fields = (
            'id', 'title', 'description', 'owner',
            'file', 'uploaded_at', 'processed'
        )
