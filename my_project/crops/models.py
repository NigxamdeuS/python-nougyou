from django.db import models
from django.contrib.auth.models import User

class Crop(models.Model):
    STAGE_CHOICES = [
        ('seedling', '苗'),
        ('growing', '生育中'),
        ('flowering', '開花'),
        ('fruiting', '結実'),
        ('ready', '収穫期'),
    ]

    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='作物名')
    variety = models.CharField(max_length=100, verbose_name='品種')
    planting_date = models.DateField(verbose_name='播種日')
    expected_harvest_date = models.DateField(verbose_name='収穫予定日')
    current_stage = models.CharField(
        max_length=20, 
        choices=STAGE_CHOICES,
        default='seedling',
        verbose_name='生育段階'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GrowthRecord(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField(verbose_name='記録日')
    photo = models.ImageField(upload_to='growth_photos/', blank=True, null=True)
    notes = models.TextField(verbose_name='備考')
    created_at = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    ITEM_TYPES = [
        ('seed', '種子'),
        ('fertilizer', '肥料'),
        ('pesticide', '農薬'),
        ('tool', '道具'),
    ]

    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='資材名')
    item_type = models.CharField(
        max_length=20,
        choices=ITEM_TYPES,
        verbose_name='種類'
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='数量'
    )
    unit = models.CharField(max_length=20, verbose_name='単位')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Harvest(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    harvest_date = models.DateField(verbose_name='収穫日')
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='収穫量'
    )
    unit = models.CharField(max_length=20, verbose_name='単位')
    revenue = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='収益'
    )
    notes = models.TextField(blank=True, null=True, verbose_name='備考')
    created_at = models.DateTimeField(auto_now_add=True)