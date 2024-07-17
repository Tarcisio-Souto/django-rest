#from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Store
from .serializer import StoreSerializer

@api_view(['GET', 'POST'])
def list_stores(request):
    if request.method == 'GET':
        people = Store.objects.all()
        serializer = StoreSerializer(people, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def search_upt_delete(request, id):
    try:
        store = Store.objects.get(id=id)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StoreSerializer(store)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        serializer = StoreSerializer(store)
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




