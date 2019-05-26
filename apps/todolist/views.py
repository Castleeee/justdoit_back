#-*-coding:utf-8-*-
from django.shortcuts import render

from .models import ItemInfo,ItemContent
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

class ItemContentListView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        itemContent= ItemContent.objects.all()
        itemContent_json = ItemInfoSerializer(itemContent, many=True)
        return Response(itemContent_json.data)
