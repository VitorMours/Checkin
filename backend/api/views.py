from .serializers import CustomJWTSerializer, JourneySerializer, UserSerializer
from .models import User, Journey
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .utils import validate_json_header



class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs) -> Response:
        if validate_json_header(request):
            return super().list(request, *args, **kwargs)
        return Response({"Requisition problem": "Wrong Content-Type Header"}, status=status.HTTP_400_BAD_REQUEST)


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

    def list(self, request, *args, **kwargs) -> Response:
        if validate_json_header(request):
            return super().list(request, *args, **kwargs)
        return Response({"Requisition problem": "Wrong Content-Type Header"}, status=status.HTTP_400_BAD_REQUEST)


class CustomJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer

