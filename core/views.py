from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import render
from .models import Grove, Harvest, MaintenanceLog
from .serializers import GroveSerializer, HarvestSerializer, MaintenanceLogSerializer

# API Views
@api_view(['GET'])
def dashboard_stats(request):
    """Get dashboard statistics for olive groves"""
    total_groves = Grove.objects.count()
    total_trees = sum(g.tree_count for g in Grove.objects.all())
    total_harvest = sum(h.quantity for h in Harvest.objects.all())
    active_groves = Grove.objects.filter(status='Active').count()

    return Response({
        "total_groves": total_groves,
        "active_groves": active_groves,
        "total_trees": total_trees,
        "total_harvest": total_harvest,
    })

@api_view(['GET'])
def grove_list_api(request):
    """Get all groves as JSON"""
    groves = Grove.objects.all()
    serializer = GroveSerializer(groves, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def grove_detail_api(request, pk):
    """Get details of a specific grove"""
    try:
        grove = Grove.objects.get(pk=pk)
    except Grove.DoesNotExist:
        return Response({'error': 'Grove not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = GroveSerializer(grove)
    return Response(serializer.data)

@api_view(['GET'])
def harvest_list_api(request):
    """Get all harvests as JSON"""
    harvests = Harvest.objects.all()
    serializer = HarvestSerializer(harvests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def maintenance_log_list_api(request):
    """Get all maintenance logs as JSON"""
    logs = MaintenanceLog.objects.all()
    serializer = MaintenanceLogSerializer(logs, many=True)
    return Response(serializer.data)

# Web Views
def home(request):
    """Home page showing dashboard"""
    total_groves = Grove.objects.count()
    total_trees = sum(g.tree_count for g in Grove.objects.all())
    total_harvest = sum(h.quantity for h in Harvest.objects.all())
    active_groves = Grove.objects.filter(status='Active').count()
    
    context = {
        'total_groves': total_groves,
        'active_groves': active_groves,
        'total_trees': total_trees,
        'total_harvest': total_harvest,
    }
    return render(request, 'core/home.html', context)

def groves_list(request):
    """List all groves"""
    groves = Grove.objects.all()
    context = {'groves': groves}
    return render(request, 'core/groves_list.html', context)

def grove_detail(request, pk):
    """Show details of a specific grove"""
    try:
        grove = Grove.objects.get(pk=pk)
    except Grove.DoesNotExist:
        return render(request, 'core/404.html', {}, status=404)
    
    harvests = grove.harvests.all()
    maintenance_logs = grove.maintenance_logs.all()
    
    context = {
        'grove': grove,
        'harvests': harvests,
        'maintenance_logs': maintenance_logs,
    }
    return render(request, 'core/grove_detail.html', context)
