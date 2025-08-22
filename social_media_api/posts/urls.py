from django.urls import path
from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet, LikePostView, UnlikePostView

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

posts_router = routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = router.urls + posts_router.urls + [
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
]
