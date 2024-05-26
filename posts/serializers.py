from rest_framework import serializers
from posts.models import PostItem

class PostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostItem
        fields = '__all__'
