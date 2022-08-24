from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.serializers import MobileSerializer
from mobapi.models import mobiles




class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=mobiles.objects.all()
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class MobileDetailView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = mobiles.objects.get(id=id)
        serializer = MobileSerializer(qs)
        return Response(data=serializer.data)

