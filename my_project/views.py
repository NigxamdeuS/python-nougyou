from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import YourModel  # あなたのモデルをインポート

@login_required
def delete_item(request, id):
    item = get_object_or_404(YourModel, id=id)
    # ユーザーが削除権限を持っているか確認
    if item.user != request.user:  # もしアイテムにユーザーフィールドがある場合
        messages.error(request, '削除権限がありません。')
        return redirect('index')
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, '正常に削除されました。')
        return redirect('index')