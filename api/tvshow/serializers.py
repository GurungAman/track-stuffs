from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from tvshow.models import TvShow


class TvShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TvShow
        fields = ('id', 'name', 'status', 'user', 'season',
                  'episode', 'added_at', 'updated_at')
        validators = [
            UniqueTogetherValidator(
                queryset=TvShow.objects.all(),
                fields=['user', 'name'],
                message='Unique name required.'
            )
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)
