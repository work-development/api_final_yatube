from rest_framework import serializers
from .models import Post, Comment, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')#, 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    following = serializers.CharField(source='following.username')
    class Meta:
        fields = ('user', 'following')
        model = Follow
# class FollowSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         fields = ('username', 'following')
#         model = Follow

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'id')
        model = Group
