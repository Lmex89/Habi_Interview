from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Furniture.models import StatusHistory, Property, Status
from Furniture.serializers import  StatusHistorySerializer
from Furniture.constants import get_queryset_raw, query, long_query, VALID_FILTER_KEY
# Create your views here.


class FurnitureList(APIView):

    def get(self, request):

        if len(self.request.query_params) == 0:
            status_history_items = StatusHistory.objects.prefetch_related('property','status').raw(
                query
            )
            
            lista_items = StatusHistorySerializer(status_history_items,many=True).data
            return Response(
                dict(
                    data=lista_items
                ),
                status=status.HTTP_200_OK
            )
       
        key_queries = list(self.request.query_params.keys())
        
        
        query_long = get_queryset_raw(long_query,key_queries,self.request.query_params)

        
        status_history_items = StatusHistory.objects.prefetch_related('property','status').raw(
            query_long    
        )
            
        lista_items = StatusHistorySerializer(status_history_items,many=True).data
        
        return Response(
            dict(
                data=lista_items
            ), 
            status=status.HTTP_200_OK
        )
