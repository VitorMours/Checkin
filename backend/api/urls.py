from django.urls import path
from rest_framework import routers
#  ManagerViewSet,
from .views import UserViewSet, CustomJWTView
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import CustomJWTSerializer
router = routers.SimpleRouter()
router.register(r"users", UserViewSet)
# router.register(r"managers", ManagerViewSet)

urlpatterns = [
    path("token/", CustomJWTView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls