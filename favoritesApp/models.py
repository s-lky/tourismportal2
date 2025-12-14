from django.db import models
from django.contrib.auth.models import User
from attractionsApp.models import Attraction

class Favorite(models.Model):
    """用户收藏"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, verbose_name="景点")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="收藏时间")
    
    class Meta:
        unique_together = ('user', 'attraction')  # 确保用户不能重复收藏同一个景点
        verbose_name = "收藏"
        verbose_name_plural = "收藏"
    
    def __str__(self):
        return f"{self.user.username} - {self.attraction.name}"
