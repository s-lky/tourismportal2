from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from attractionsApp.models import Attraction

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="下单用户")
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, verbose_name="预订景点")
    visit_date = models.DateField(verbose_name="游玩日期")
    quantity = models.PositiveIntegerField(default=1, verbose_name="票数")
    status = models.CharField(max_length=20, default='paid', verbose_name="状态") # 简化处理，默认已支付