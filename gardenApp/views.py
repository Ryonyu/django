from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import (NoteBook)
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request, 'index.html')

##################################################################################################
# notebook
##################################################################################################
# 一覧
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
