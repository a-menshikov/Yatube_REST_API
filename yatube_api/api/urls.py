from django.urls import include, path
from rest_framework import routers

from .views import CommentsViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentsViewSet,
                basename='comment')
router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
