from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TripPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="发布用户")
    title = models.CharField(max_length=200, verbose_name="攻略标题")
    content = models.TextField(verbose_name="路线详情")
    days = models.IntegerField(verbose_name="建议游玩天数")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="发布时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "旅游攻略"
        verbose_name_plural = "旅游攻略"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title