from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SnippetViewSet, TagViewSet

router = DefaultRouter()
router.register(r"snippets", SnippetViewSet)
router.register(r"tags", TagViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
