from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from cart.serializers import CartSerializer
from cart.models import CartModel


class CartViews:

    # Create Cart class
    class CartCreateAPIView(generics.CreateAPIView):
        serializer_class = CartSerializer

        def post(self, request):
            new_cart_serializer = self.get_serializer(data=request.data)
            if new_cart_serializer.is_valid():
                new_cart_serializer.save()
                return Response({'message': 'cart_created', 'cart': new_cart_serializer.data},
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'bad_request', 'logs': new_cart_serializer.errors})

    class CartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = CartSerializer
        queryset = CartModel.objects.filter()

        def put(self, request, pk=None):
            cart_to_update = self.get_queryset().filter(id=pk).first()
            if cart_to_update:
                cart_updated = self.serializer_class(cart_to_update, data=request.data)
                if cart_updated.is_valid():
                    cart_updated.save()
                    return Response({'message': 'cart_updated', 'cart': cart_updated.data},
                                    status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'bad_request', 'logs': cart_updated.errors},
                                    status=status.HTTP_400_BAD_REQUEST)

            else:
                return Response({'error': 'cart_not_found'}, status=status.HTTP_400_BAD_REQUEST)