from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from cart.serializers import CartItemSerializer
from cart.models import CartItemModel


class CartItemViews:

    class CartItemCreateAPIView(generics.CreateAPIView):
        serializer_class = CartItemSerializer

        def post(self, request):
            new_cart_item = self.serializer_class(data=request.data)
            if new_cart_item.is_valid():
                new_cart_item.save()
                return Response({'message': 'cart_item_created', 'cart_item': new_cart_item.data},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'bad_request', 'logs': new_cart_item.errors},
                                status=status.HTTP_400_BAD_REQUEST)

    class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = CartItemSerializer
        queryset = CartItemModel.objects.filter()

        def put(self, request, pk=None):
            cart_item_to_update = self.get_queryset().filter(id=pk).first()
            if cart_item_to_update:
                cart_item_updated = self.serializer_class(cart_item_to_update, data=request.data)
                if cart_item_updated.is_valid():
                    cart_item_updated.save()
                    return Response({'message': 'cart_item_updated', 'cart': cart_item_updated.data},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'bad_request', 'logs': cart_item_updated.errors},
                                    status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'error': 'cart_item_not_found'}, status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk=None):
            cart_item = self.get_queryset().filter(id=pk).first()
            if cart_item:
                cart_item.delete()
                return Response({'message': 'cart_item_deleted'},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'cart_item_not_found'}, status=status.HTTP_400_BAD_REQUEST)