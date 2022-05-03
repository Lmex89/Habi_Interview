
from rest_framework import serializers
from Furniture.models import Property, StatusHistory

class PropterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class StatusHistorySerializer(serializers.ModelSerializer):
    
    property = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    
    def get_status(self, instance):
        
        return instance.status.name
    
    def get_property(self, instance):
        
        return dict(
            price=instance.property.price,
            address=instance.property.address,
            city=instance.property.city,
            description=instance.property.description,
            year=instance.property.year)
        
    
    class Meta:
        model = StatusHistory
        fields = '__all__'