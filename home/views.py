from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.http import FileResponse, Http404
from django.conf import settings
import os

from .serializers import HomeContentSerializer
from .models import HomeContent

class HomeContentView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     content = HomeContent.objects.all()
    #     serializer = HomeContentSerializer(content, many=True)
    #     return Response(serializer.data)
    
    def get(self, request, *args, **kwargs):
        image_name = kwargs.get('image_name', None)
        if image_name:
            return self.get_image(request, image_name)
        else:
            content = HomeContent.objects.all()
            serializer = HomeContentSerializer(content, many=True)
            return Response(serializer.data)

    
    # def get_image(self, request, image_name, format=None):
    #     # This part handles image serving
    #     if settings.DEBUG:
    #         image_path = os.path.join(settings.BASE_DIR, 'konferenzbackend', 'static', 'img', image_name)
    #     else:
    #         image_path = os.path.join(settings.STATIC_ROOT, 'img', image_name)
    #     try:
    #         with open(image_path, 'rb') as file:
    #             return FileResponse(file, content_type='image/jpeg')
    #     except FileNotFoundError:
    #         raise Http404("Image does not exist")
    
    
    def get_image(self, request, image_name, format=None):
        # This part handles image serving
        image_path = os.path.join(settings.MEDIA_ROOT, 'img', image_name)
        try:
            with open(image_path, 'rb') as file:
                return FileResponse(file, content_type='image/jpeg')
        except FileNotFoundError:
            raise Http404("Image does not exist")