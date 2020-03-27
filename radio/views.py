from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions, generics, status, mixins
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from radio.models import Hits, Artists
from radio.serializers import (HitsSerializer, HitsDetailsSerializer,
                               CreateHitsSerializer, UpdateHitsSerializer)


class NewHitsCreateList(APIView):
    def get(self, request):
        hits_list = Hits.objects.all().order_by('-created_at')[:20]
        serializer = HitsSerializer(hits_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CreateHitsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCreateHitsView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Hits.objects.all().order_by('-created_at')[:20]

    def get(self, request, *args, **kwargs):
        self.serializer_class = HitsSerializer
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.serializer_class = CreateHitsSerializer
        return self.create(request, *args, **kwargs)


class ModifyHitView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'title_url'
    serializer_class = HitsDetailsSerializer
    def get_queryset(self):
        queryset = Hits.objects.get(title_url=self.kwargs['title_url'])
        return queryset





@api_view(['GET', 'PUT', 'DELETE'])
def hit_details(request, title_url):
    try:
        hit = Hits.objects.get(title_url=title_url)
    except Hits.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HitsDetailsSerializer(hit)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateHitsSerializer(hit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

