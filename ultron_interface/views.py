from rest_framework import viewsets
from .pagination import SizeOffsetPagination
from rest_framework.response import Response

from .serializers import CourtSnippetSerializer
from .models import CourtSnippet


class CourtSnippetViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourtSnippetSerializer
    queryset = CourtSnippet.objects.using('snippets').all()

    def list(self, request, *args, **kwargs):
        return Response({'adsad': 'asdsad'})