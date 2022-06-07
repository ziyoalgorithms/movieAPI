
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Movie API",
        default_version="v1.0.01",
        description="Swagger docs for RestAPI",
        contact=openapi.Contact("Anvarov Ziyodulloxon <example_name@gmail.com>")
    ),
    public=True,
    permission_classes=(AllowAny, )
)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studio.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]
