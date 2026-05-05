from django.contrib import admin
from .models import Grove, Harvest, MaintenanceLog

class HarvestInline(admin.TabularInline):
    model = Harvest
    extra = 1

class MaintenanceLogInline(admin.TabularInline):
    model = MaintenanceLog
    extra = 1

@admin.register(Grove)
class GroveAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'variety', 'tree_count', 'area_hectares', 'status')
    list_filter = ('status', 'variety', 'irrigation_type', 'soil_type')
    search_fields = ('name', 'location')
    inlines = [HarvestInline, MaintenanceLogInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location', 'image_url')
        }),
        ('Grove Details', {
            'fields': ('variety', 'tree_count', 'area_hectares', 'planting_year')
        }),
        ('Management', {
            'fields': ('irrigation_type', 'soil_type', 'status')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
    )

@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ('grove', 'harvest_date', 'quantity', 'quality_grade', 'oil_yield')
    list_filter = ('harvest_date', 'quality_grade', 'grove')
    search_fields = ('grove__name',)
    date_hierarchy = 'harvest_date'

@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ('grove', 'task_type', 'date', 'completed', 'cost')
    list_filter = ('task_type', 'date', 'completed', 'grove')
    search_fields = ('grove__name', 'description')
    date_hierarchy = 'date'
