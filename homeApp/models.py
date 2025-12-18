from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    """用户资料扩展模型"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="用户", related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', verbose_name="头像", null=True, blank=True, default='avatars/default.png')
    phone = models.CharField(max_length=20, verbose_name="电话", null=True, blank=True)
    address = models.CharField(max_length=200, verbose_name="地址", null=True, blank=True)
    bio = models.TextField(max_length=500, verbose_name="个人简介", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        verbose_name = "用户资料"
        verbose_name_plural = "用户资料"
    
    def __str__(self):
        return f"{self.user.username}的资料"
    
    def get_avatar_url(self):
        """获取头像URL，如果没有则返回默认头像"""
        if self.avatar:
            return self.avatar.url
        return '/static/img/default-avatar.png'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """当用户创建时自动创建用户资料"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """当用户保存时自动保存用户资料"""
    if hasattr(instance, 'profile'):
        instance.profile.save()
