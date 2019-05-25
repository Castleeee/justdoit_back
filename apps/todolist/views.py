#-*-coding:utf-8-*-
from django.shortcuts import render

from .models import ItemInfo
from .serializers import ItemInfoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class ItemInfoListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        item= ItemInfo.objects.all()
        item_json = ItemInfoSerializer(item, many=True)
        return Response(item_json.data)
