from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mycups/', views.CustomerRecordListView.as_view(), name='customer-view-cups'),
    path('manage-cups/', views.BusinessCupListView.as_view(), name='business-manage-cups'),
    path('request-cups/', views.request_cups, name='business-request-cups'),
    path('receive-cups/', views.receive_cups, name='business-receive-cups'),
]