# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from base.models import Items
# from .serializers import ItemSerializer
#
# @api_view(['GET'])
# def getData(request):
#     #person = {'name':'Abed', 'age':24}
#     items = Items.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def addItem(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import AssetSerializer, EmployeeSerializer
from .models import Asset, Employee

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

    @action(detail=True, methods=['post'])
    def assign(self, request, pk=None):
        asset = self.get_object()
        employee_id = request.data.get('employee_id')
        employee = Employee.objects.get(pk=employee_id)
        asset.assigned_to = employee
        asset.save()
        return Response({'status': 'Asset assigned'})

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer




