from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lesson, LessonMaterial
from .serializers import LessonSerializer, LessonMaterialSerializer


class LessonMaterialView(APIView):
    def get(self, request, pk=None):
        key = 'lessons_materials'
        if pk is not None:
            lessons_material = get_object_or_404(LessonMaterial.objects.all(), pk=pk)
            serializer = LessonMaterialSerializer(lessons_material)
            key = 'lesson_material'
        else:
            lessons_material = LessonMaterial.objects.all()
            serializer = LessonMaterialSerializer(lessons_material, many=True)
        return Response({key: serializer.data})

    def post(self, request):
        lesson_material = request.data.get('lesson_material')
        serializer = LessonMaterialSerializer(data=lesson_material)
        if serializer.is_valid(raise_exception=True):
            lesson_material_saved = serializer.save()
        return Response({"success": "Lesson material'{}' created successfully".format(lesson_material_saved.title)})

    def put(self, request, pk):
        saved_lesson_material = get_object_or_404(LessonMaterial.objects.all(), pk=pk)
        data = request.data.get('lesson_material')
        serializer = LessonMaterialSerializer(instance=saved_lesson_material, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            lesson_material_saved = serializer.save()
        return Response({
            "success": "Lesson material '{}' updated successfully".format(lesson_material_saved.title)
        })

    def delete(self, request, pk):
        lesson_material = get_object_or_404(LessonMaterial.objects.all(), pk=pk)
        lesson_material.delete()
        return Response({
            "message": "Lesson material with id `{}` has been deleted.".format(pk)
        }, status=204)


class LessonView(APIView):
    def get(self, request, pk=None):
        key = 'lessons'
        if pk is not None:
            lesson = get_object_or_404(Lesson.objects.prefetch_related('materials').all(), pk=pk)
            serializer = LessonSerializer(lesson)
            key = 'lesson'
        else:
            lessons = Lesson.objects.prefetch_related('materials').all()
            serializer = LessonSerializer(lessons, many=True)
        return Response({key: serializer.data})

    def post(self, request):
        lesson = request.data.get('lesson')
        serializer = LessonSerializer(data=lesson)
        if serializer.is_valid(raise_exception=True):
            lesson_saved = serializer.save()
        return Response({"success": "Lesson '{}' created successfully".format(lesson_saved.title)})

    def put(self, request, pk):
        saved_lesson = get_object_or_404(Lesson.objects.all(), pk=pk)
        data = request.data.get('lesson')
        serializer = LessonSerializer(instance=saved_lesson, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            lesson_saved = serializer.save()
        return Response({
            "success": "Lesson '{}' updated successfully".format(lesson_saved.title)
        })

    def delete(self, request, pk):
        lesson = get_object_or_404(Lesson.objects.all(), pk=pk)
        lesson.delete()
        return Response({
            "message": "Lesson with id `{}` has been deleted.".format(pk)
        }, status=204)
