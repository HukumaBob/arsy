from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="ARSY API",
      default_version='v1',
      description="This is the ARSY API version",
      terms_of_service="https://rcmag.pro/",
      contact=openapi.Contact(email="office@rcbi.pro"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/v1/', include('api.urls', namespace='api')),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.jwt')),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=2), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=2), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=2), name='schema-redoc'),
]
