from django import forms
from .models import TripPlan

class TripPlanForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'multiple': True,
            'accept': 'image/*'
        }),
        required=False,
        label='攻略图片',
        help_text='最多可上传10张图片（按住Ctrl键可选择多张）'
    )
    
    class Meta:
        model = TripPlan
        fields = ['title', 'content', 'days', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入攻略标题'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 15,
                'placeholder': '请输入详细的旅游路线、景点推荐、住宿建议、美食推荐等内容...'
            }),
            'days': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 30
            })
        }
        labels = {
            'title': '攻略标题',
            'content': '路线详情',
            'days': '建议游玩天数',
            'image': '攻略封面图',
        }
    
    def clean_days(self):
        days = self.cleaned_data.get('days')
        if days and (days < 1 or days > 30):
            raise forms.ValidationError('游玩天数必须在1-30天之间')
        return days
    
    def clean(self):
        cleaned_data = super().clean()
        # 验证图片数量
        if 'images' in self.files:
            images = self.files.getlist('images')
            if len(images) > 10:
                raise forms.ValidationError({'images': '最多只能上传10张图片，请重新选择'})
        return cleaned_data

