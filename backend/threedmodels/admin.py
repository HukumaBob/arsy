from django.contrib import admin

from .models import ThreeDModel

@admin.register(ThreeDModel)
class ThreeDModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'owner',
        'uploaded_at',
        'processed',
    )
    list_filter = ('owner',)
    search_fields = ('owner', 'uploaded_at',)

