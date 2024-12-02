from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Crop, GrowthRecord, Inventory, Harvest
from .forms import CropForm, GrowthRecordForm, InventoryForm, HarvestForm

@login_required
def crop_list(request):
    crops = Crop.objects.filter(farmer=request.user)
    return render(request, 'crops/crop_list.html', {'crops': crops})

@login_required
def crop_add(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.farmer = request.user
            crop.save()
            messages.success(request, '作物が追加されました。')
            return redirect('crops:crop_list')
    else:
        form = CropForm()
    return render(request, 'crops/crop_form.html', {'form': form})

@login_required
def crop_detail(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id, farmer=request.user)
    growth_records = crop.growthrecord_set.all().order_by('-date')
    harvests = crop.harvest_set.all().order_by('-harvest_date')
    return render(request, 'crops/crop_detail.html', {
        'crop': crop,
        'growth_records': growth_records,
        'harvests': harvests
    })

@login_required
def growth_record_add(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id, farmer=request.user)
    if request.method == 'POST':
        form = GrowthRecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.crop = crop
            record.save()
            messages.success(request, '生育記録が追加されました。')
            return redirect('crops:crop_detail', crop_id=crop.id)
    else:
        form = GrowthRecordForm()
    return render(request, 'crops/growth_record_form.html', {
        'form': form,
        'crop': crop
    })

@login_required
def inventory_list(request):
    inventory_items = Inventory.objects.filter(farmer=request.user)
    return render(request, 'crops/inventory_list.html', {
        'inventory_items': inventory_items
    })

@login_required
def inventory_add(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.farmer = request.user
            item.save()
            messages.success(request, '在庫アイテムが追加されました。')
            return redirect('crops:inventory_list')
    else:
        form = InventoryForm()
    return render(request, 'crops/inventory_form.html', {'form': form})

@login_required
def inventory_edit(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id, farmer=request.user)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            messages.success(request, '在庫情報が更新されました。')
            return redirect('crops:inventory_list')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'crops/inventory_form.html', {'form': form})

@login_required
def harvest_add(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id, farmer=request.user)
    if request.method == 'POST':
        form = HarvestForm(request.POST)
        if form.is_valid():
            harvest = form.save(commit=False)
            harvest.crop = crop
            harvest.save()
            messages.success(request, '収穫記録が追加されました。')
            return redirect('crops:crop_detail', crop_id=crop.id)
    else:
        form = HarvestForm()
    return render(request, 'crops/harvest_form.html', {
        'form': form,
        'crop': crop
    })

@login_required
def crop_edit(request, crop_id):
    crop = get_object_or_404(Crop, id=crop_id, farmer=request.user)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            messages.success(request, '作物情報が更新されました。')
            return redirect('crops:crop_detail', crop_id=crop.id)
    else:
        form = CropForm(instance=crop)
    return render(request, 'crops/crop_form.html', {
        'form': form,
        'crop': crop,
        'is_edit': True
    })

@login_required
def harvest_list(request):
    # ユーザーの全ての作物の収穫記録を取得
    harvests = Harvest.objects.filter(
        crop__farmer=request.user
    ).select_related('crop').order_by('-harvest_date')
    
    # 収穫記録を月ごとにグループ化
    harvests_by_month = {}
    total_revenue = 0
    
    for harvest in harvests:
        month_key = harvest.harvest_date.strftime('%Y年%m月')
        if month_key not in harvests_by_month:
            harvests_by_month[month_key] = {
                'harvests': [],
                'monthly_revenue': 0
            }
        harvests_by_month[month_key]['harvests'].append(harvest)
        harvests_by_month[month_key]['monthly_revenue'] += harvest.revenue
        total_revenue += harvest.revenue

    return render(request, 'crops/harvest_list.html', {
        'harvests_by_month': harvests_by_month,
        'total_revenue': total_revenue
    }) 