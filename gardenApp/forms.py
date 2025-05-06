from django import forms
from .models import  NoteBook

class NoteBookForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('エアプランツ・プロメリア','エアプランツ・プロメリア'),
        ('サボテン・多肉植物', 'サボテン・多肉植物'),        # 多肉植物
        ('観葉植物', '観葉植物'),                          # 観葉植物、食虫植物、熱帯植物
        ('クレマチス','クレマチス'),
        ('ラン','ラン'),                                # ラン
        ('セントポーリア','セントポーリア'),
        ('バラ','バラ'),
        ('樹木・花木','樹木・花木'),                    # コニファー、庭木・花木
        ('果樹','果樹'),                                # 果樹
        ('水生植物','水生植物'),                          # 水生植物
        ('山野草','山野草'),                              # 山野草
        ('ハーブ','ハーブ'),                            # ハーブ
        ('野菜','野菜'),                                # 野菜
        ('球根','球根'),                                # 球根
        ('リーフプランツ','リーフプランツ'),              # グラス、シダ
        ('草花・鉢花','草花・鉢花'),                      # 草花
        ('雑草','雑草'),
        ('不明','不明'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="カテゴリ")

    #MONTH_CHOICES = [(f'{i}月', f'{i}月') for i in range(1, 13)]
    MONTH_CHOICES = [('1月', '1月'), ('2月', '2月'), ('3月', '3月'), ('4月', '4月'), ('5月', '5月'), ('6月', '6月'), ('7月', '7月'), ('8月', '8月'), ('9月', '9月'), ('10月', '10月'), ('11月', '11月'), ('12月', '12月'),('不明','不明'),('ALL','ALL')]
    season = forms.ChoiceField(choices=MONTH_CHOICES, label="月")

    #FLOOR_CHOICES = [(f'{i}F', f'{i}F') for i in range(1, 10)]
    FLOOR_CHOICES = [('1F', '1F'), ('2F', '2F'), ('3F', '3F'), ('4F', '4F'), ('5F', '5F'), ('6F', '6F'), ('7F', '7F'), ('8F', '8F'), ('9F', '9F'),('不明','不明')]

    floor = forms.ChoiceField(choices=FLOOR_CHOICES, label="フロア")    
    class Meta:
        model = NoteBook
        fields = ['title', 'category','image', 'image2','content','url', 'season', 'floor', 'area', 'memo']
        labels = {
            'title': '名称',
            'category': 'カテゴリ',
            'content': '説明',
            'image': '画像',
            'image2':'画像2',
            'url': 'URL',
            'season': '季節',
            'floor': 'フロア',
            'area': 'エリア',
            'memo': 'メモ',
        }
