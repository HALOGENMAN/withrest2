from django.shortcuts import render
from .serializers import ASerializers
from .models import A
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import View
from rest_framework import authentication,permissions
# Create your views here.


@csrf_exempt
def test2(request):
    if request.method == "GET":
        q = A.objects.all()
        s = ASerializers(q,many=True)
        return JsonResponse(s.data,safe=False)
   
    elif request.method == "POST":
        data = JSONParser().parse(request)
        s = ASerializers(data=data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=201)
        else:
            return JsonResponse(s.errors,status=404)

@csrf_exempt
def test21(request,id):
    try:
        q = A.objects.get(id=id)
    except Exception as e:
        return HttpResponse("now found")
    
    if request.method =="GET":
        s = ASerializers(q)
        return JsonResponse(s.data)

    elif request.method =="PUT":
        data = JSONParser().parse(request)
        s = ASerializers(q,data=data)
        if s.is_valid():
            s.save()
            return JSONParse(s.data,status=200)
        else:
            return JSONParse(s.error,status=400)
    elif request.method =="DELETE":
        q.delete()
        return HttpResponse(status=204)
