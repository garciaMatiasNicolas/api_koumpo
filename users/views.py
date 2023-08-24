from rest_framework import viewsets
from rest_framework.response import Response
from users.serializers import UserSerializer
from users.models import UserModel as User
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request):
        new_user = self.get_serializer(data=request.data)
        if new_user.is_valid():
            new_user.save()
            return Response({'message': 'user_created', 'user': new_user.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'bad_request', 'logs': new_user.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user_to_update = self.get_queryset().filter(id=pk).first()

        if user_to_update:
            data_updated = self.get_serializer(user_to_update, data=request.data)
            if data_updated.is_valid():
                data_updated.save()
                return Response({'message': 'user_updated', 'user': data_updated.data},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'bad_request', 'logs': data_updated.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': 'user_not_found'},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_to_delete = self.get_queryset().filter(id=pk).first()

        if user_to_delete:
            user_to_delete.delete()
            return Response({'message': 'user_deleted'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'user_not_found'},
                            status=status.HTTP_400_BAD_REQUEST)