from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .serializers import Bserializers
from .models import B
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.

class pool(generics.GenericAPIView,mixins.CreateModelMixin,
                                    mixins.ListModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.DestroyModelMixin):

    serializer_class = Bserializers
    queryset = B.objects.all()
    lookup_field = "id"
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id) 
        else:           
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)
        
    def perform_create(self,serializer):
        serializer.save(created_by=self.request.user)

    def delete(self,request,id=None):
        return self.destroy(request,id)


