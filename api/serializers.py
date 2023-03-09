# from rest_framework import serializers
# from base.models import Items
#
# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Items
#         fields = '__all__'

from rest_framework import serializers
from .models import Asset, Employee

class AssetSerializer(serializers.ModelSerializer):
    assigned_to = serializers.StringRelatedField()

    class Meta:
        model = Asset
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'