from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
    """美食模型 - 用于图鉴展示"""
    RATING_CHOICES = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )
    
    name = models.CharField(max_length=100, verbose_name="美食名称")
    image = models.ImageField(upload_to='foods/', verbose_name="美食图片")
    rating = models.IntegerField(choices=RATING_CHOICES, default=5, verbose_name="推荐指数")
    description = models.TextField(blank=True, verbose_name="美食描述")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "美食"
        verbose_name_plural = "美食"
    
    def __str__(self):
        return self.name


class FoodRecommendation(models.Model):
    """美食推荐模型 - 用户投稿"""
    STATUS_CHOICES = (
        ('pending', '待审核'),
        ('approved', '已通过'),
        ('rejected', '已拒绝'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="推荐用户")
    food_name = models.CharField(max_length=100, verbose_name="美食名称")
    location = models.CharField(max_length=200, verbose_name="地点")
    reason = models.TextField(verbose_name="推荐理由")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="审核状态")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="投稿时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "美食推荐"
        verbose_name_plural = "美食推荐"
    
    def __str__(self):
        return f"{self.user.username} - {self.food_name}"
