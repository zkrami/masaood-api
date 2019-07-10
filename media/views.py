from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin ,  RetrieveModelMixin
from rest_framework.response import Response
import rest_framework.status
from rest_framework.exceptions import ParseError
from .models import Media
from .serializers import MediaSerializer
# Create your views here.


# ViewSet which inherit default list and retrieve implementation
class MediaViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin ):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = ()

    def create(self, request):
        try:
            file = request.data['file']
        except KeyError:
            raise ParseError('File field is required ')
        # content_type
        # name
        media = Media.objects.create(file=file)
        serializer = self.get_serializer(media)
        print(vars(media))
        print(vars(serializer))
        return Response(serializer.data,  status=rest_framework.status.HTTP_201_CREATED)
