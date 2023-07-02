from rest_framework import serializers

from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'nota',
            'criacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):
    # Nested relationshipp - usada para poucos dados, mostra todas as avaliações dos cursos na mesma tela
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    # HyperLinked Related Field - cria links das avalições dos cursos. Usada para quantidade média de dados
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='avaliacao-detail')

    # Primary Key Related Fiel - usada para muitos dados. Mostra apenas o id das avaliações dos cursos
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )
