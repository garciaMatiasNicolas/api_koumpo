from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from cart.serializers import CartSerializer
from cart.models.model_cart import CartModel

class CartViewSets(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = CartModel.objects.all()

    def create(self, request):
        new_cart = self.get_serializer(data=request.data)

        if new_cart.is_valid():
            new_cart.save()
            return Response({'message': 'cart_created', 'cart': new_cart.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'bad_request', 'logs': new_cart.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        cart_to_update = self.get_queryset().filter(id=pk).first()

        if cart_to_update:
            data_updated = self.get_serializer(cart_to_update, data=request.data)
            if data_updated.is_valid():
                data_updated.save()
                return Response({'message': 'cart_updated', 'cart': data_updated.data},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'bad_request', 'logs': data_updated.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': 'cart_not_found'},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cart_to_delete = self.get_queryset().filter(id=pk).first()

        if cart_to_delete:
            cart_to_delete.delete()
            return Response({'message': 'cart_deleted'},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'cart_not_found'},
                            status=status.HTTP_400_BAD_REQUEST)
