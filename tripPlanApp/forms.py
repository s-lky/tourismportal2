from django import forms
from .models import TripPlan

 #定义一个支持多选的文件上传组件类
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class TripPlanForm(forms.ModelForm):
    images = forms.FileField(
        # 2.这里把 widget=forms.FileInput 改为 widget=MultipleFileInput
        widget=MultipleFileInput(attrs={
            'class': 'form-control',
            'multiple': True,  #这里的 multiple 仍然需要保留给前端 HTML 用
            'accept': 'image/*'
        }),
        required=False,
        label='攻略图片',
        help_text='最多可上传10张图片（按住Ctrl键可选择多张）'
    )
    
    class Meta:
        model = TripPlan
        #这里的 'image' 是封面图（单张），上面的 'images' 是相册（多张），逻辑没问题
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
        #验证图片数量
        #这里用 self.files 来获取文件数据
        if 'images' in self.files:
            images = self.files.getlist('images')
            if len(images) > 10:
                raise forms.ValidationError('最多只能上传10张图片，请重新选择')
        return cleaned_data