from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from rest_framework.exceptions import ValidationError
from .models import Product

@api_view(['GET'])
def get_info(request):
    data = {
        'succes': True,
        'message': "Everything is OK"
    }
    return Response(data)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "succes": True,
            "message": "Product created successfully",
            "data": serializer.data
        }
        return Response(data)
    raise ValidationError(serializer.errors)

@api_view(['GET'])
def list_product(request):
    products = Product.objects.all()[::-1]
    if len(products) == 0:
        raise ValidationError("No Data")
    serializer = ProductSerializer(products, many=True)
    data = {
        'succes': True,
        'message': "Everything is OK",
        'products': serializer.data
    }
    return Response(data)

@api_view(['GET'])
def detail_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if product is None:
        raise ValidationError("No Data")
    serializer = ProductSerializer(products,)
    data = {
        'succes': True,
        'message': "Product",
        'products': serializer.data
    }
    return Response(data)

@api_view(['PUT'])
def update_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if product is None:
        raise ValidationError("No Data")
    serializer = ProductSerializer(product, request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "succes": True,
            "message": "Product created successfully",
            "data": serializer.data
        }
        return Response(data)
    raise ValidationError(serializer.errors)


@api_view(['PUT'])
def patch_product(request, pk):
    product = Product.objects.filter(pk=pk).first()
    if product is None:
        raise ValidationError("No Data")
    serializer = ProductSerializer(product, request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        data = {
            "succes": True,
            "message": "Product created successfully",
            "data": serializer.data
        }
        return Response(data)
    raise ValidationError(serializer.errors)