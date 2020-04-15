from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов"""

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        lessons = validated_data.pop('lessons')
        course = Course.objects.create(**validated_data)
        for lesson in lessons:
            course.lessons.add(lesson)
        return course

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.position = validated_data.get('position', instance.position)
        instance.direction = validated_data.get('direction', instance.direction)
        if validated_data.get('lessons') is not None:
            if len(validated_data.get('lessons')) > 0:
                for lesson in validated_data.get('lessons'):
                    instance.lessons.add(lesson)
            else:
                instance.lessons.clear()

        instance.save()

        return instance
