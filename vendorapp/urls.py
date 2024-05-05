from django.urls import path
from vendorapp.views import vendorcreate,vendorretrieveupdatedestroy,purchasecreate,purchaseretrieveupdatedestroy,VendorPerformanceView

urlpatterns=[
    path('vendor/',vendorcreate.as_view(),name='vendor_create'),
    path('vendor/<int:pk>/',vendorretrieveupdatedestroy.as_view(),name='vendor_retrieve_update_destroy'),
    path('vendor/<int:id>/performance/',VendorPerformanceView.as_view(),name='vendor_performance'),
    path('purchase_order/',purchasecreate.as_view(),name='purchase_create'),
    path('purchase_order/<int:pk>/',purchaseretrieveupdatedestroy.as_view(),name='purchase_retrieve_update_delete'),


]