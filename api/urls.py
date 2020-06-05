from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import PostViewSet, CommentsViewSet, FollowViewSet, GroupViewSet
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
commets_router = routers.NestedSimpleRouter(router, r'posts', lookup='posts')
commets_router.register(r'comments', CommentsViewSet, basename='comments')

router_1 = DefaultRouter()
router_1.register('follow', FollowViewSet, basename='follow')


router_2 = DefaultRouter()
router_2.register('group', GroupViewSet, basename='group')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router_1.urls)),
    path('', include(router_2.urls)),
    path('', include(router.urls)),
    path('', include(commets_router.urls)),
]

# router = DefaultRouter()
# router.register('posts', PostViewSet, basename='posts')
# # router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
# commets_router = routers.NestedSimpleRouter(router, r'posts', lookup='posts')
# commets_router.register(r'comments', CommentsViewSet, basename='comments')
# # router.register('follow', FollowViewSet, basename='follow')
# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(commets_router.urls)),
#     path('follow/', FollowViewSet.as_view(), name='follow'),
#     path('group/', GroupViewSet.as_view(), name='group')
# ]

urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]
