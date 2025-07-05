from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import (NoteBook,CustomUser)
from .forms import (NoteBookForm)
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpRequest


PAGENATION_NUM = 100

PASSWORD = "gardenMax"  # 任意のパスワードを設定


import os
import zipfile
from io import BytesIO
from django.http import HttpResponse
from django.conf import settings

def download_output_images(request):
    # media/output_imagesの絶対パスを取得
    output_dir = os.path.join(settings.MEDIA_ROOT, 'output_images')
    # ZIPファイルをメモリ上に作成
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for filename in os.listdir(output_dir):
            file_path = os.path.join(output_dir, filename)
            if os.path.isfile(file_path):
                zip_file.write(file_path, arcname=filename)
    zip_buffer.seek(0)
    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=output_images.zip'
    return response



# utils.py などに保存（または views.py に直接書いてもOK）
from django.shortcuts import redirect

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('custom_user_id'):
            return redirect('login')  # 未ログインならログイン画面へ
        return view_func(request, *args, **kwargs)
    
    return wrapper


# Create your views here.
def index(request):
    return render(request, 'index.html')

def register_view(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        hashed_password = make_password(raw_password)

        CustomUser.objects.create(username=username, password=hashed_password)
        return redirect('notebook_list')  # 登録後にリダイレクト
    return render(request, 'register.html')

def login_view(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']

        try:
            user = CustomUser.objects.get(username=username)
            if check_password(raw_password, user.password):
                # セッションにログイン情報を保存
                request.session['custom_user_id'] = user.id
                return redirect('notebook_list')  # ログイン成功後にリダイレクト
            else:
                error = "ログイン情報に誤りがあります。"
        except CustomUser.DoesNotExist:
            error = "ログイン情報に誤りがあります。"
        return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')



##################################################################################################
# notebook
##################################################################################################
# 一覧

@custom_login_required
def notebook_list(request):
    models = NoteBook.objects.all()

    search_query = request.GET.get('search', '')
    search_type = request.GET.get('search_type','')

    # 検索
    search_query = request.GET.get('search', '')

    if search_type=='name':
       if search_query:
           models = models.filter(title__icontains=search_query)    
    elif search_type=='category':
       if search_query:
           models = models.filter(category__icontains=search_query)
    elif search_type=='floor':
       if search_query:
           models = models.filter(floor__icontains=search_query)
    elif search_type=='season':
       if search_query:
           models = models.filter(season__icontains=search_query)
    elif search_type=='area':
       if search_query:
           models = models.filter(area__icontains=search_query)
    elif search_type=='memo':
       if search_query:
           models = models.filter(memo__icontains=search_query)
    elif search_type=='content':
       if search_query:
           models = models.filter(content__icontains=search_query)
    # ソート
    sort_by = request.GET.get('sort', 'title')
    models = models.order_by(sort_by)

    # ページネーション
    paginator = Paginator(models, PAGENATION_NUM)  # 1ページ10件表示
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    from django.utils.timezone import now
    # 本日登録された植物
    today = now().date()
    today_notebooks = models.filter(created_at__date=today)
    today_count = today_notebooks.count()
    
    total_count = models.count()
    return render(request, 'notebook_list.html', {'page_obj': page_obj,'total_count':total_count,'today_count':today_count})
# 作成
def notebook_create(request):
    if request.method == 'POST':
        form = NoteBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notebook_list')
    else:
        form = NoteBookForm()
    return render(request, 'notebook_create.html', {'form': form})
# 編集
def notebook_edit(request, id):
    notebook_model = get_object_or_404(NoteBook, pk=id)
    
    if request.method == 'POST':
        form = NoteBookForm(request.POST, request.FILES,instance=notebook_model)
        if form.is_valid():
            form.save()
            return redirect('notebook_list')  # 編集後に一覧ページにリダイレクト
    else:
        form = NoteBookForm(instance=notebook_model)
    
    return render(request, 'notebook_edit.html', {'form': form, 'notebook_model': notebook_model})
# 削除
def notebook_delete(request, id):
    notebook_model = get_object_or_404(NoteBook, pk=id)
    
    if request.method == 'POST':
        notebook_model.delete()
        return redirect('notebook_list')  # 削除後に一覧ページにリダイレクト
    
    return render(request, 'notebook_confirm_delete.html', {'notebook_model': notebook_model})
