from django.db import models

class Grove(models.Model):
    VARIETIES = [
        ("Koroneiki", "Koroneiki"),
        ("Arbequina", "Arbequina"),
        ("Picual", "Picual"),
        ("Frantoio", "Frantoio"),
    ]

    STATUS = [
        ("Active", "Active"),
        ("Dormant", "Dormant"),
        ("New", "New Planting"),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    variety = models.CharField(max_length=50, choices=VARIETIES)
    tree_count = models.IntegerField()
    area_hectares = models.FloatField()
    planting_year = models.IntegerField()
    irrigation_type = models.CharField(max_length=50, default="Drip")
    soil_type = models.CharField(max_length=50, default="Loam")
    status = models.CharField(max_length=20, choices=STATUS, default="Active")
    notes = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class Harvest(models.Model):
    grove = models.ForeignKey(Grove, on_delete=models.CASCADE, related_name='harvests')
    harvest_date = models.DateField()
    quantity = models.FloatField(help_text="Quantity in kilograms")
    quality_grade = models.CharField(max_length=50, default="Standard")
    oil_yield = models.FloatField(null=True, blank=True, help_text="Oil yield in percentage")
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grove.name} - {self.harvest_date}"

    class Meta:
        ordering = ['-harvest_date']


class MaintenanceLog(models.Model):
    TASK_TYPES = [
        ("Pruning", "Pruning"),
        ("Irrigation", "Irrigation"),
        ("Fertilization", "Fertilization"),
        ("Pest Control", "Pest Control"),
        ("Disease Treatment", "Disease Treatment"),
        ("Other", "Other"),
    ]

    grove = models.ForeignKey(Grove, on_delete=models.CASCADE, related_name='maintenance_logs')
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    date = models.DateField()
    description = models.TextField()
    cost = models.FloatField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.grove.name} - {self.task_type} ({self.date})"

    class Meta:
        ordering = ['-date']
