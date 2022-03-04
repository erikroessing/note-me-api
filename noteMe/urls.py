from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Notes.views import NotesViewSet, ItemsViewSet


router = DefaultRouter()
router.register('note', NotesViewSet)
router.register('item', ItemsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
