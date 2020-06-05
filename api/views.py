from django.shortcuts import render
from rest_framework import viewsets, status, filters
from .models import User, Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import ValidationError




class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #queryset = Post.objects.all()--- если не указать в router.register('posts', PostViewSet, basename='posts') basename то будит ошибка если не разкоментировать эту строчку

    def get_queryset(self):
        if not self.request.query_params.get('group'):
            return Post.objects.all()
        return Post.objects.filter(group=self.request.query_params.get('group'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentsViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_post_with_specific_key(self):
        post = get_object_or_404(Post, id=self.kwargs['posts_pk'])
        return post

    def get_queryset(self):
        queryset = Comment.objects.filter(post=self.get_post_with_specific_key()).all()
        return queryset


class FollowViewSet(viewsets.ModelViewSet):

    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username', ]

    def perform_create(self, serializer):
        following = get_object_or_404(
            User,
            username=self.request.data.get('following')
        )
        user = self.request.user
        follows = self.queryset.filter(user=user, following=following)
        if follows.exists():
            raise ValidationError(f'У вас уже есть подписка на {following}.')
        if user == following:
            raise ValidationError('Нельзя подписаться на самого себя.')
        serializer.save(user=user, following=following)

class GroupViewSet(viewsets.ModelViewSet):

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(slug=self.request.query_params.get('slug'))
