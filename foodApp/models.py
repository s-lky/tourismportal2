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


class Restaurant(models.Model):
    """餐厅模型 - 老字号探店"""
    CITY_CHOICES = (
        ('guangzhou', '广州'),
        ('shenzhen', '深圳'),
        ('foshan', '佛山'),
        ('dongguan', '东莞'),
        ('zhuhai', '珠海'),
        ('zhongshan', '中山'),
        ('jiangmen', '江门'),
        ('huizhou', '惠州'),
        ('other', '其他'),
    )
    
    name = models.CharField(max_length=100, verbose_name="餐厅名称")
    city = models.CharField(max_length=20, choices=CITY_CHOICES, verbose_name="所在城市", default='guangzhou')
    address = models.CharField(max_length=200, verbose_name="详细地址")
    image = models.ImageField(upload_to='restaurants/', verbose_name="餐厅图片")
    description = models.TextField(verbose_name="餐厅介绍")
    signature_dishes = models.CharField(max_length=200, verbose_name="招牌菜", help_text="多个菜品用逗号分隔")
    opening_hours = models.CharField(max_length=100, default="10:00-22:00", verbose_name="营业时间")
    phone = models.CharField(max_length=20, blank=True, verbose_name="联系电话")
    view_count = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "餐厅"
        verbose_name_plural = "餐厅"
    
    def __str__(self):
        return self.name
    
    def get_signature_dishes_list(self):
        """获取招牌菜列表"""
        return [dish.strip() for dish in self.signature_dishes.split(',') if dish.strip()]


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
