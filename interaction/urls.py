from django.urls import path
from interaction.views import business, customer, index

urlpatterns = [
    path('', index.index, name='index'),
    path('customer/mycups/', customer.CustomerRecordListView.as_view(), name='customer-view-cups'),
    path('business/manage-cups/', business.BusinessCupListView.as_view(), name='business-manage-cups'),
    path('business/request-cups/', business.request_cups, name='business-request-cups'),
    path('business/receive-cups/', business.receive_cups, name='business-receive-cups'),
]