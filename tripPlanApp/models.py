from django.db import models

# Create your models here.
class TripPlan(models.Model):
    title = models.CharField(max_length=200, verbose_name="攻略标题")
    content = models.TextField(verbose_name="路线详情")
    days = models.IntegerField(verbose_name="建议游玩天数")
    created_at = models.DateTimeField(auto_now_add=True)