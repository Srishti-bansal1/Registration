from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets ,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Registration
from .serializer import RegSerializer

class RegViewSet (viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegSerializer
    
    @action(detail=False, methods=["GET"],url_path='show')
    def getCustom(self, request):
        queryset = Registration.objects.all()
        serializer = RegSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    
    @action(detail=False, methods=["POST"],url_path='create')
    def created(self, request):
        dataReceived = request.data 
        serializer = RegSerializer(data = request.data)

        if Registration.objects.filter(**dataReceived).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        
    @action(detail=True , methods=['PUT'],url_path='modify')
    def modify(self,request,pk=None):
        queryset  = Registration.objects.get(pk=pk)
        serializer = RegSerializer(instance = queryset,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        
    @action(detail=False , methods=['DELETE'],url_path='delete_all')
    def remove_all(self,request):
        Registration.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)