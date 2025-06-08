from django.db import models

# Create your models here.
class NoteBook(models.Model):
    title = models.CharField(max_length=255)  # ノートブックのタイトル
    content = models.TextField(null=True)  # ノートブックの内容

    category = models.CharField(max_length=255,null=True,blank=True)  # ノートブックのタイトル

    season = models.CharField(max_length=255,null=True,blank=True)  # ノートブックのタイトル
    floor = models.CharField(max_length=255,null=True,blank=True)  # ノートブックのタイトル
    area = models.CharField(max_length=255,null=True,blank=True)  # ノートブックのタイトル

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    image = models.ImageField(upload_to='output_images/',null=True, blank=True)  # 出力画像
    image2 = models.ImageField(upload_to='output_images/',null=True, blank=True)  # 出力画像
    memo = models.CharField(max_length=255,null=True,blank=True)  # ノートブックのタイトル

    url = models.URLField(null=True,blank=True)  # URL
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時

class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # ハッシュ済みのパスワードを保存
