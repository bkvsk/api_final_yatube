from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet


router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register('follow', FollowViewSet, basename='follow')
router.register('group', GroupViewSet)

urlpatterns = [
    path(
        '/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair',
    ),
    path(
        '/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh',
    ),
    path('v1/', include(router.urls)),
]
