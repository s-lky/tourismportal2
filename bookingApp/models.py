from django.db import models
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import User
from attractionsApp.models import Attraction

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', '待支付'),
        ('paid', '已支付'),
        ('cancelled', '已取消'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="下单用户")
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, verbose_name="预订景点")
    visit_date = models.DateField(verbose_name="游玩日期")
    quantity = models.PositiveIntegerField(default=1, verbose_name="票数")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paid', verbose_name="状态")
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name="创建时间")
    
    def __str__(self):
        return f"{self.user.username} - {self.attraction.name} - {self.visit_date}"
    
    @property
    def total_price(self):
        """计算总价"""
        return self.attraction.price * self.quantity