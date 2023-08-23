from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UserSerializer
from users.models import UserModel as User
from rest_framework import status


class UserEndpoints:
    @api_view(['GET'])
    def read_all(request):
        # If method is get type
        if request.method == 'GET':
            # Get all users and return as JSON
            query = User.objects.all()
            users_serializer = UserSerializer(query, many=True)
            return Response(users_serializer.data, status=status.HTTP_200_OK)
        # If method isn't get type
        else:
            return Response({'error': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @api_view(['GET', 'DELETE', 'PUT'])
    def detail_user(request, pk):
        query = User.objects.filter(id=pk).first()

        if request.method == 'GET':
            users_serializer = UserSerializer(query)
            return Response(users_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            user = UserSerializer(query, data=request.data)
            if user.is_valid():
                user.save()
                return Response(data=user.data, status=status.HTTP_200_OK)
            else:
                return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            query.delete()
            return Response({'message': 'user deleted successfully'})

        else:
            return Response({'error': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @api_view(['POST'])
    def create(request):
        # If method is post type
        if request.method == 'POST':
            # Create new user
            user = UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response(user.data, status=status.HTTP_201_CREATED)
            else:
                return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
        # If method isn't post type
        else:
            return Response({'error': 'method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)