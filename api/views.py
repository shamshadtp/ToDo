from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializer import Taskserializer
from reminder.models import Task

# Create your views here.

class TaskViewset(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Task.objects.all()
        serializers=Taskserializer(qs,many=True)
        return Response(data=serializers.data)
    
    def create(self,request,*args,**kwargs):
        serializers=Taskserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return Response(data=serializers.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=Taskserializer(qs)
        return Response(data=serializers.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        serializers=Taskserializer(data=request.data,instance=qs)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data)
        return Response(serializers.errors)
    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Task.objects.get(id=id)
        if qs.user==request.user:
            qs.delete()
            return Response()