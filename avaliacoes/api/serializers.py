from rest_framework.serializers import ModelSerializer

from avaliacoes.models import Avaliacao


class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'usuario', 'nota', 'comentario', 'data')
