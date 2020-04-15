from rest_framework import serializers

from .models import Direction


class DirectionSerializer(serializers.ModelSerializer):
    """Сериализатор для напривлений"""

    class Meta:
        model = Direction
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.position = validated_data.get('position', instance.position)
        instance.save()

        return instance
