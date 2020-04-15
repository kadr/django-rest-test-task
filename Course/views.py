from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer


class CourseView(APIView):
    def get(self, request, pk=None):
        key = 'courses'
        if pk is not None:
            course = get_object_or_404(Course.objects.prefetch_related('direction', 'lessons').all(), pk=pk)
            serializer = CourseSerializer(course)
            key = 'course'
        else:
            courses = Course.objects.prefetch_related('direction', 'lessons').all()
            serializer = CourseSerializer(courses, many=True)
        return Response({key: serializer.data})

    def post(self, request):
        course = request.data.get('course')
        serializer = CourseSerializer(data=course)
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({"success": "Course '{}' created successfully".format(course_saved.title)})

    def put(self, request, pk):
        saved_course = get_object_or_404(Course.objects.all(), pk=pk)
        data = request.data.get('course')
        serializer = CourseSerializer(instance=saved_course, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({
            "success": "Course '{}' updated successfully".format(course_saved.title)
        })

    def delete(self, request, pk):
        course = get_object_or_404(Course.objects.all(), pk=pk)
        course.delete()
        return Response({
            "message": "Course with id `{}` has been deleted.".format(pk)
        }, status=204)
