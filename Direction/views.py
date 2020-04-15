from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Direction
from .serializers import DirectionSerializer


class DirectionView(APIView):
    def get(self, request):
        directions = Direction.objects.all()
        serialiser = DirectionSerializer(directions, many=True)
        return Response({"directions": serialiser.data})

    def post(self, request):
        direction = request.data.get('direction')
        serializer = DirectionSerializer(data=direction)
        if serializer.is_valid(raise_exception=True):
            direction_saved = serializer.save()
        return Response({"success": "Direction '{}' created successfully".format(direction_saved.title)})

    def put(self, request, pk):
        saved_direction = get_object_or_404(Direction.objects.all(), pk=pk)
        data = request.data.get('direction')
        serializer = DirectionSerializer(instance=saved_direction, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            direction_saved = serializer.save()
        return Response({
            "success": "Direction '{}' updated successfully".format(direction_saved.title)
        })

    def delete(self, request, pk):
        direction = get_object_or_404(Direction.objects.all(), pk=pk)
        direction.delete()
        return Response({
            "message": "Direction with id `{}` has been deleted.".format(pk)
        }, status=204)