from rest_framework import serializers
from .models import Grove, Harvest, MaintenanceLog

class HarvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harvest
        fields = ['id', 'grove', 'harvest_date', 'quantity', 'quality_grade', 'oil_yield', 'notes']

class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = ['id', 'grove', 'task_type', 'date', 'description', 'cost', 'completed']

class GroveSerializer(serializers.ModelSerializer):
    harvests = HarvestSerializer(many=True, read_only=True)
    maintenance_logs = MaintenanceLogSerializer(many=True, read_only=True)
    
    class Meta:
        model = Grove
        fields = [
            'id', 'name', 'location', 'variety', 'tree_count',
            'area_hectares', 'planting_year', 'irrigation_type',
            'soil_type', 'status', 'notes', 'image_url',
            'created_at', 'updated_at', 'harvests', 'maintenance_logs'
        ]
