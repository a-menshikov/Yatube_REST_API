from django.urls import include, path
from rest_framework import routers

from .views import CommentsViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentsViewSet,
                basename='comment')
router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
