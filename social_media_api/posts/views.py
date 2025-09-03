from rest_framework import permissions, viewsets, filters, status, generics
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from notifications.models import Notification
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .pagination import PostCommentPagination

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostCommentPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        following_users = request.user.following.all()  

        posts = Post.objects.filter(author__in=following_users).order_by("-created_at")  

        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like, created = Like.objects.get_or_create(post=post, author=user)

        if created:
            if post.author != user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=user,
                    verb="liked your post",
                    content_type=ContentType.objects.get_for_model(Post),
                    object_id=post.id
                )
            return Response({"message": "Liked"}, status=status.HTTP_201_CREATED)
        else:
            like.delete()
            return Response({"message": "Unliked"}, status=status.HTTP_200_OK)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = PostCommentPagination

    def get_queryset(self):
        post_id = self.kwargs.get("post_pk")
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_pk")
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # required line
        like, created = Like.objects.get_or_create(user=request.user, post=post)  # required line

        if not created:
            # already liked → unlike it
            like.delete()
            return Response({"message": "Unliked"}, status=status.HTTP_200_OK)

        # if new like → create notification
        if post.author != request.user:  # don’t notify if liking own post
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target_post=post
            )

        return Response({"message": "Liked"}, status=status.HTTP_201_CREATED)
