# pylint: disable=missing-docstring,has-no-member
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import PostItemSerializer
from .models import PostItem

class PostItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        posts = PostItem.objects.filter(author=request.user)
        serializer = PostItemSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostItemUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        post = PostItem.objects.get(pk=pk)
        checked = request.data.get('checked')
        if checked is not None:
            post.checked = checked
            post.save()
            serializer = PostItemSerializer(post)
            return Response(serializer.data)
        else:
            return Response({"error": "Invalid or missing 'checked' value"}, status=400)
        
    def delete(self, request, pk, format=None):
        post = PostItem.objects.get(pk=pk)
        post.delete()
        return Response(status=204)

    
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })