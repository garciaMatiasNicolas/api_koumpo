from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductModel
from products.serializers import ProductSerializer


class ProductsViews:
    # Create and List Product class
    class ProductListCreateAPIView(generics.ListCreateAPIView):
        serializer_class = ProductSerializer
        queryset = ProductModel.objects.all()  # Get all products

        def post(self, request):
            product_created = self.get_serializer(data=request.data)  # Serialize data from post
            if product_created.is_valid():  # Verify if data is valid and then save it
                product_created.save()
                return Response({'message': 'created', 'product': product_created.data},
                                status=status.HTTP_201_CREATED)  # Return products
            else:
                return Response({'error': 'bad_request', 'logs': product_created.errors},
                                status=status.HTTP_400_BAD_REQUEST)  # Return errors

    # Detail product class
    class ProductDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ProductSerializer
        queryset = ProductModel.objects.filter()  # Get product detail

        def put(self, request, pk=None):
            product_to_update = self.get_queryset().filter(id=pk).first()  # Get product

            if product_to_update:  # If product exists
                data_product_updated = self.serializer_class(product_to_update, request.data)
                if data_product_updated.is_valid():  # If data is valid update product
                    data_product_updated.save()
                    return Response({'message': 'updated', 'product_updated': data_product_updated.data},
                                    status=status.HTTP_200_OK)
                else:  # Else return errors
                    return Response({'error': 'bad_request', 'logs': data_product_updated.errors},
                                    status=status.HTTP_400_BAD_REQUEST)

            else:  # Else return not found
                return Response({'error': 'product_not_found'},
                                status=status.HTTP_400_BAD_REQUEST)

        def delete(self, request, pk=None):
            product_to_delete = self.get_queryset().filter(id=pk).first()  # Get product

            if product_to_delete:  # If product exists deleted
                product_to_delete.delete()
                return Response({'message': 'deleted'},
                                status=status.HTTP_200_OK)

            else:  # Else return not found
                return Response({'error': 'product_not_found'},
                                status=status.HTTP_400_BAD_REQUEST)