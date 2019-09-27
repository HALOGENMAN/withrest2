from django.shortcuts import render
from test3.serializers import BSerializers
from .models import B
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

class poollistViwe(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = BSerializers
    queryset = B.objects.all()
    lookup_field = "id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return update(request,id)

class pool(APIView):
    def get(self,request,format=None):
        q = B.objects.all()
        s = BSerializers(q,many = True)
        return Response(s.data)
    def post(self,request,format=None):
        s = BSerializers(data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors)
    
class pool1(APIView):
    
    def get_object(self,id):#this is important  function
        try:
            return B.objects.get(id=id)
        except Exception:
            return Response("not found")
        
    def get(self,request,id=None):
        q = self.get_object(id)
        s = BSerializers(q)
        return Response(s.data)

    def put(self,request,id=None):
        q = self.get_object(id)
        s = BSerializers( q , data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.error)
    def delete(self,request,id=None):
        q = self.get_object(id)
        q.delete()
        return HttpResponse("happy birth day modi")