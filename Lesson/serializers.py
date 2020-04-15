from rest_framework import serializers

from Lesson.models import Lesson, LessonMaterial


class LessonMaterialSerializer(serializers.ModelSerializer):
    """Сериализатор для материалов курсов"""

    class Meta:
        model = LessonMaterial
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        return LessonMaterial.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.material1 = validated_data.get('material1', instance.material1)
        instance.material2 = validated_data.get('material2', instance.material2)
        instance.material3 = validated_data.get('material3', instance.material3)
        instance.material4 = validated_data.get('material4', instance.material4)

        instance.save()

        return instance


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов"""

    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        materials = validated_data.pop('materials')
        lesson = Lesson.objects.create(**validated_data)
        for material in materials:
            lesson.materials.add(material)

        return lesson

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.anons = validated_data.get('anons', instance.anons)
        instance.description = validated_data.get('description', instance.description)
        instance.link_to_video = validated_data.get('link_to_video', instance.link_to_video)
        instance.link_to_file = validated_data.get('link_to_file', instance.link_to_file)
        if validated_data.get('materials') is not None:
            if len(validated_data.get('materials')) > 0:
                for material in validated_data.get('materials'):
                    instance.materials.add(material)
            else:
                instance.materials.clear()

        instance.save()

        return instance
