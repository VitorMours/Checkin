from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from checkin.infra.db.models import User 
from checkin.core.usecases.create_user import CreateUser
from checkin.infra.db.repositories import UserRepository

from .serializers import UserSerializer

class UserView(APIView):
    """
    User view to manipulate the users data
    """
    def get(self, request) -> None:
        """
        Return a list with the classes in the database
        """
        repository = UserRepository()
        users = repository.get_all()
        serialized_data = UserSerializer(users, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request) -> None:
        """
        Create a new element inside of the group
        """
        print(request)
        repository = UserRepository()
        use_case = CreateUser(repository=repository)

        serialized_data = UserSerializer(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        validated_data = serialized_data.validated_data
        
        user = use_case.execute(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_201_CREATED)
    
    def put(self, request, pk) -> None: 
        """
        Update the element of the user based on the pk
        """
        # TODO: Create the service to update the user based on the pk search 