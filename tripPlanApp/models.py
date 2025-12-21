from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TripPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发布用户", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="攻略标题")
    content = models.TextField(verbose_name="路线详情")
    days = models.IntegerField(verbose_name="建议游玩天数")
    image = models.ImageField(upload_to='tripPlans/', verbose_name="攻略图片", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "旅游攻略"
        verbose_name_plural = "旅游攻略"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class TripPlanImage(models.Model):
    """旅游攻略图片模型 - 支持多图显示"""
    trip_plan = models.ForeignKey(TripPlan, on_delete=models.CASCADE, related_name='images', verbose_name="旅游攻略")
    image = models.ImageField(upload_to='tripPlans/gallery/', verbose_name="图片")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "攻略图片"
        verbose_name_plural = "攻略图片"
    
    def __str__(self):
        return f"{self.trip_plan.title} - 图片{self.order}"