from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from game.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'status', 'user', 'added_at', 'updated_at')
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                fields=['user', 'name'],
                message='Unique name required.'
            )
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
