from django.urls import path
from rest_framework import routers
from .views import UserViewSet, CustomJWTView, JourneyViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .serializers import CustomJWTSerializer


router = routers.SimpleRouter()
router.register(r"users", UserViewSet)
router.register(r"journey", JourneyViewSet)

urlpatterns = [
    path("auth/token/", CustomJWTView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += router.urls