from django.urls import include, path
from rest_framework import routers
from apiAI import views

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'consultas', views.QuerysViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api_schema', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api-schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api-schema'}
        ), name='swagger-ui'),
    
]