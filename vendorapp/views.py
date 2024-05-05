from django.shortcuts import render
from vendorapp.serializers import VendorSerializer,PurchaseSerializer
from vendorapp.models import vendor,purchaseorder
from rest_framework import generics
from rest_framework.response import Response



# Create your views here.

class vendorcreate(generics.ListCreateAPIView):
    queryset = vendor.objects.all()
    serializer_class = VendorSerializer

class vendorretrieveupdatedestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = vendor.objects.all()
    serializer_class = VendorSerializer


class purchasecreate(generics.ListCreateAPIView):
    queryset = purchaseorder.objects.all()
    serializer_class = PurchaseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        vendor_id = self.request.query_params.get('vendor')
        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)
        return queryset



class purchaseretrieveupdatedestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = purchaseorder.objects.all()
    serializer_class = PurchaseSerializer


class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        performance_data = {
            'vendor_id':instance.id,
            'name':instance.name,
            'on_time_delivery_rate': instance.on_time_delivery_rate,
            'quality_rating_avg': instance.quality_rating_avg,
            'average_response_time': instance.average_response_time,
            'fulfillment_rate': instance.fulfillment_rate,
        }
        return Response(performance_data)







