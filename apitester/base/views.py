from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.serializers import ItemSerializers
from . models import ItemModel
from rest_framework import status
# Create your views here.
@api_view(['GET'])
def itemlist(request):
    item = ItemModel.objects.all()
    serializer = ItemSerializers(item,many = True)
    return Response(serializer.data)


    
    