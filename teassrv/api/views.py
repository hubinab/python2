from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Brand, Tea
from .serialize import  BrandSerializer, TeaSerializer, TeaSerializer2
#import logging

#logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_brands (request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def get_post_Teas (request):
    if request.method == 'GET':
        teas = Tea.objects.all()
        serializer = TeaSerializer2(teas, many=True)
        return Response(serializer.data)
    else:
        serializer = TeaSerializer(data=request.data)
        if serializer.is_valid():
            tea = serializer.save()
            serializer = TeaSerializer2 (tea)
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def create_brand (request):
    serializer = BrandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_tea (request):
    serializer = TeaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE' ])
def brand_detail (request, pk):
    try:
        user = Brand.objects.get (pk=pk)
    except Brand.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        serializer = BrandSerializer (user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BrandSerializer (user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE' ])
def tea_detail (request, pk):
    try:
        tea = Tea.objects.get (pk=pk)
    except Tea.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
 
    if request.method == 'GET':
        serializer = TeaSerializer (tea)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeaSerializer (tea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer = TeaSerializer2 (tea)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
