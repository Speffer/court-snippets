from rest_framework import serializers
from .models import CourtSnippet


class CourtSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourtSnippet
        fields = [
            'numeracao_unica', 'recorte', 'id', 'codigo_diario', 'data_publicacao'
        ]