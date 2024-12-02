from django import forms
from .models import Crop, GrowthRecord, Inventory, Harvest

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'variety', 'planting_date', 'expected_harvest_date', 'current_stage']
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
            'expected_harvest_date': forms.DateInput(attrs={'type': 'date'}),
        }

class GrowthRecordForm(forms.ModelForm):
    class Meta:
        model = GrowthRecord
        fields = ['date', 'photo', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'item_type', 'quantity', 'unit']

class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['harvest_date', 'quantity', 'unit', 'revenue', 'notes']
        widgets = {
            'harvest_date': forms.DateInput(attrs={'type': 'date'}),
        } 