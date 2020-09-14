from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from API.models import CoffeMachine,CoffePod
from API.serializers import CoffeMachineSerializer,CoffePodSerializer
# API design 




class CoffeMachineListView(generics.ListAPIView):
    queryset = CoffeMachine.objects.all()
    serializer_class = CoffeMachineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_type', 'product_type','water_line_compatible']


class CoffePodListView(generics.ListAPIView):
    queryset = CoffePod.objects.all()
    serializer_class = CoffePodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product_type', 'coffee_flavor','pack_size']


class CoffeMachineCreateView(generics.CreateAPIView):
    queryset         = CoffeMachine.objects.all()
    serializer_class = CoffeMachineSerializer

    def post(self,request, format = None):
 
        serializer = CoffeMachineSerializer(data=request.data)
        # permission_classes = [IsAuthenticated]
        

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,   status=status.HTTP_400_BAD_REQUEST)

class CoffePodCreateView(generics.CreateAPIView):
    queryset         = CoffePod.objects.all()
    serializer_class = CoffePodSerializer

    def post(self,request, format = None):
 
        serializer = CoffePodSerializer(data=request.data)
        # permission_classes = [IsAuthenticated]
        

        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,   status=status.HTTP_400_BAD_REQUEST)