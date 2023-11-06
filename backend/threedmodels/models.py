from pathlib import Path
from django.contrib.auth.models import User
from django.db import models


def file_upload_path(instance, filename):
    file_extension = Path(filename).suffix
    if file_extension in ['.fbx', ]:
        return Path('filmbox', filename)
    elif file_extension in ['.obj', ]:
        return Path('obj', filename)
    elif file_extension in ['.glb', '.gltf', ]:
        return Path('gltf', filename)
    else:
        return Path('other', filename)


class ThreeDModel(models.Model):
    title = models.CharField(verbose_name='Model name', max_length=120)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        verbose_name='3DModel owner',
        related_name='three_d_models',
        on_delete=models.CASCADE,
    )
    file = models.FileField(upload_to=file_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
