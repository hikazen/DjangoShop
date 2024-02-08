from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Product, Category, Tag, Review
from .serializers import ProductSerializer, CategorySerializer, TagSerializer, ReviewSerializer, ReviewCreateSerializer


# class ProductList(APIView):
#
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryList(APIView):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)


class ProductDetail(APIView):

    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)



class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# class CategoryDetail(APIView):
#
#
#     def get(self, request, pk, *args, **kwargs):
#         category = Category.objects.get(id=pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)


class ProductCreate(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductUpdate(APIView):

    def put(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDelete(APIView):

    def delete(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product is not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({"message": "Product deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class CategoryDelete(APIView):

    def delete(self, request, pk, *args, **kwargs):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category is not found"}, status=status.HTTP_404_NOT_FOUND)

        category.delete()
        return Response({"message": "Category deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


class CategoryUpdate(APIView):

    def put(self, request, pk, *args, **kwargs):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(product=category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        product = Category.objects.get(id=pk)
        serializer = CategorySerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer



class ReviewCreate(CreateAPIView):

    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReviewList(ListAPIView):

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewUpdate(APIView):
    queryset = Review.objects.all()

    def patch(self, request, pk, *args, **kwargs):
        reviews = Review.objects.get(id=pk)
        serializer = ReviewSerializer(reviews, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReviewDelete(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            review = Review.objects.get(id=pk)
        except Review.DoesNotExist:
            return Response({"error": "Review is not found"}, status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response({"message": "Review has been deleted"}, status=status.HTTP_200_OK)

