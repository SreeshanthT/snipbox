from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet, Tag
from .serializers import SnippetSerializer, TagSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Snippet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def overview(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        total_count = queryset.count()

        snippets = [
            {
                "id": snippet.id,
                "title": snippet.title,
                "detail_url": reverse("snippet-detail", args=[snippet.id], request=request),
            }
            for snippet in queryset
        ]

        return Response({"total_count": total_count, "snippets": snippets})


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["get"])
    def snippets_by_tag(self, request, pk=None):
        tag = Tag.objects.get(pk=pk)
        snippets = tag.snippets.all()
        return Response(SnippetSerializer(snippets, many=True).data)
