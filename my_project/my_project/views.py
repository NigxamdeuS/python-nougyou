from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from crops.models import Crop, Inventory, Harvest

@login_required
def delete_inventory(request, id):
    item = get_object_or_404(Inventory, id=id)
    if item.farmer != request.user:
        messages.error(request, '削除権限がありません。')
        return redirect('crops:inventory_list')
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, '在庫が正常に削除されました。')
    return redirect('crops:inventory_list')

@login_required
def delete_crop(request, id):
    crop = get_object_or_404(Crop, id=id)
    if crop.farmer != request.user:
        messages.error(request, '削除権限がありません。')
        return redirect('crops:crop_list')
    
    if request.method == 'POST':
        crop.delete()
        messages.success(request, '作物が正常に削除されました。')
    return redirect('crops:crop_list')

@login_required
def delete_harvest(request, id):
    harvest = get_object_or_404(Harvest, id=id)
    if harvest.crop.farmer != request.user:
        messages.error(request, '削除権限がありません。')
        return redirect('crops:harvest_list')
    
    if request.method == 'POST':
        harvest.delete()
        messages.success(request, '収穫記録が正常に削除されました。')
    return redirect('crops:harvest_list') 