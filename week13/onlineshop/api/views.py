from django.shortcuts import render

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProductOrder, Offer
from .serializers import ProductOrderSerializer, OfferSerializer

from .constats import SELLER


class OfferListApiView(APIView):
    def get(self, request):
        offers = Offer.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductOrderApiView(APIView):
    def get(self, request):
        orders = ProductOrder.objects.all()
        serializer = ProductOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductOrderSerializer(data=request.data)
        if request.user.role == SELLER:
            return Response({'error': 'salesmen can not create order'})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductOrderDetailApiView(APIView):

    def get_object(self, pk):
        try:
            return ProductOrder.objects.get(id=pk)
        except ProductOrder.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_object(pk)
        serializer = ProductOrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order = self.get_object(pk)
        serializer = ProductOrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)