from django.db import models

class Attraction(models.Model):
    # 定义区域选项
    REGION_CHOICES = (
        ('yue_bei', '粤北'),
        ('yue_xi', '粤西'),
        ('yue_nan', '粤南'),
        ('yue_dong', '粤东'),
        ('gang_ao', '港澳'),
    )

    name = models.CharField(max_length=100, verbose_name="景点名称")
    region = models.CharField(max_length=20, choices=REGION_CHOICES, verbose_name="所属区域")
    description = models.TextField(verbose_name="景点介绍")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="门票价格")
    # 需要配置Media设置才能上传图片，后面会讲
    image = models.ImageField(upload_to='attractions/', verbose_name="封面图")
    
    def __str__(self):
        return self.name