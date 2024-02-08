from _ast import Delete

from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import ProductList, CategoryList, ProductDetail, CategoryDetail, ProductCreate, CategoryCreate, \
    ProductUpdate, ProductDelete, CategoryDelete, CategoryUpdate, TagViewSet, ReviewCreate, ReviewList, ReviewUpdate, \
    ReviewDelete

router = DefaultRouter()

router.register('', TagViewSet)


urlpatterns = [

    # Product
    path('products/', ProductList.as_view()),
    path('products/<int:pk>/', ProductDetail.as_view()),
    path('products/create/', ProductCreate.as_view()),
    path('products/update/<int:pk>/', ProductUpdate.as_view()),
    path('products/delete/<int:pk>/', ProductDelete.as_view()),

    # Category
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
    path('category/create/', CategoryCreate.as_view()),
    path('category/delete/<int:pk>/', CategoryDelete.as_view()),
    path('category/update/<int:pk>/', CategoryUpdate.as_view()),

    # Tag
    path('tags/', include(router.urls)),

    # Reviews
    path('reviews/create/', ReviewCreate.as_view()),
    path('reviews/', ReviewList.as_view()),
    path('reviews/update/<int:pk>/', ReviewUpdate.as_view()),
    path('reviews/delete/<int:pk>/', ReviewDelete.as_view())
]
