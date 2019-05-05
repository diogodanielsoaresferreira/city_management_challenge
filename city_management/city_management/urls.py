from django.urls import path
from django.conf.urls import include, url
from event_management import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Event Management",
      default_version='v1',
      description="Management of events in a city",
   ),
   public=True,
)

urlpatterns = [
    path('v1/events/', views.EventList.as_view()),
    path('v1/events/<int:pk>/', views.EventDetail.as_view()),
]

urlpatterns += [
    url(r'^swagger(?P<format>\.json|.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]