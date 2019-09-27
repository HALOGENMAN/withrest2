from django.shortcuts import render
from .serializers import Bserializers
from rest_framework.views import APIView
from rest_framework.response import Response
from test3.models import B
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins


class pool(generics.GenericAPIView,mixins.ListModelMixin,
                                   mixins.CreateModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.RetrieveModelMixin,
                                   mixins.DestroyModelMixin):
    serializer_class =  Bserializers
    queryset = B.objects.all()
    lookup_field ="id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    

    def post(self,request):
        return self.create(request)
    if id:
        def put(self,request,id=None):
            return self.update(request,id)
    else:
        pass
    
    def delete(self,request,id=None):
        return self.destroy(request,id)
        