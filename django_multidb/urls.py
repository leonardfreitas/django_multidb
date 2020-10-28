from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.notes.api.viewsets import NoteViewSet

router = DefaultRouter()
router.register('notes', NoteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
