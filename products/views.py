from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductModel
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

    def create(self, request):
        new_product = self.get_serializer(data=request.data)  # Serialize new product data
        if new_product.is_valid():  # If data is valid save it and then return it
            new_product.save()
            return Response({'message': 'product_created', 'product': new_product.data},
                            status=status.HTTP_201_CREATED)
        else: # Else return errors
            return Response({'error': 'bad_request', 'logs': new_product.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        product_to_update = self.get_queryset().filter(id=pk).first()

        if product_to_update:  # If product to update exists
            updated_data = self.get_serializer(product_to_update, data=request.data)  # Send updated data and save it
            if updated_data.is_valid():
                updated_data.save()
                return Response({'message': 'product_updated', 'product': updated_data.data},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'bad_request', 'logs': updated_data.errors},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'error': 'product_not_found'},
                            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product_to_delete = self.get_queryset().filter(id=pk).first()  # Get product

        if product_to_delete:  # Verify product exists and then delete
            product_to_delete.delete()
            return Response({'message': 'product_deleted'},
                            status=status.HTTP_200_OK)
        else:  # If product doesn't exists send error
            return Response({'error': 'product_not_found'},
                            status=status.HTTP_400_BAD_REQUEST)
