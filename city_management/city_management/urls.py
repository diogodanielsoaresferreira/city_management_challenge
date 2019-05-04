from django.urls import path
from django.conf.urls import include, url
from event_management import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('v1/events/', views.EventList.as_view()),
    path('v1/events/<int:pk>/', views.EventDetail.as_view()),
    path('docs/', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)