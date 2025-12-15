from django.db import models
from django.contrib.auth.models import User

class Attraction(models.Model):
    # 定义区域选项
    REGION_CHOICES = (
        ('yue_bei', '粤北'),
        ('yue_xi', '粤西'),
        ('yue_nan', '粤南'),
        ('yue_dong', '粤东'),
        ('gang_ao', '港澳'),
    )
    
    # 定义城市选项
    CITY_CHOICES = (
        ('guangzhou', '广州'),
        ('shenzhen', '深圳'),
        ('foshan', '佛山'),
        ('dongguan', '东莞'),
        ('zhuhai', '珠海'),
        ('zhongshan', '中山'),
        ('jiangmen', '江门'),
        ('huizhou', '惠州'),
        ('zhaoqing', '肇庆'),
        ('shantou', '汕头'),
        ('chaozhou', '潮州'),
        ('other', '其他'),
    )
    
    # 定义类型选项
    TYPE_CHOICES = (
        ('natural', '自然'),
        ('cultural', '人文'),
        ('mixed', '综合'),
    )

    name = models.CharField(max_length=100, verbose_name="景点名称")
    region = models.CharField(max_length=20, choices=REGION_CHOICES, verbose_name="所属区域")
    city = models.CharField(max_length=20, choices=CITY_CHOICES, verbose_name="所属城市", default='guangzhou')
    attraction_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="景点类型", default='mixed')
    description = models.TextField(verbose_name="景点介绍")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="门票价格")
    # 需要配置Media设置才能上传图片，后面会讲
    image = models.ImageField(upload_to='attractions/', verbose_name="封面图")
    opening_hours = models.CharField(max_length=200, verbose_name="开放时间", default="09:00-18:00")
    map_image = models.ImageField(upload_to='attractions/maps/', verbose_name="地图位置图", null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0, verbose_name="浏览量")
    like_count = models.PositiveIntegerField(default=0, verbose_name="点赞数")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "景点"
        verbose_name_plural = "景点"
    
    def __str__(self):
        return self.name


class AttractionImage(models.Model):
    """景点图片模型 - 支持多图轮播"""
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='images', verbose_name="景点")
    image = models.ImageField(upload_to='attractions/gallery/', verbose_name="图片")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "景点图片"
        verbose_name_plural = "景点图片"
    
    def __str__(self):
        return f"{self.attraction.name} - 图片{self.order}"


class AttractionLike(models.Model):
    """景点点赞模型"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='likes', verbose_name="景点")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="点赞时间")
    
    class Meta:
        unique_together = ('user', 'attraction')
        verbose_name = "点赞"
        verbose_name_plural = "点赞"
    
    def __str__(self):
        return f"{self.user.username} 点赞 {self.attraction.name}"