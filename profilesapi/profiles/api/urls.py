from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles.api.views import AvatarUpdateView, ProfileViewSet, ProfileStatusViewSet

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet)


# profile_list = ProfileViewSet.as_view({"get": "list"})
# profile_detail = ProfileViewSet.as_view({"get": "retrieve"})


urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
    # path("profiles/", profile_list, name='profile-list'),
    # path("profiles/<int:pk>/", profile_detail, name='profile-detail')
]