from django.urls import include, path
from rest_framework import routers
from .views import UsersViewSet, SegmentsListViewSet, ActionsViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'segments', SegmentsListViewSet)
router.register(r'actions', ActionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
