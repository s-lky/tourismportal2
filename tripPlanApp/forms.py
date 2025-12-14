from django import forms
from .models import TripPlan

class TripPlanForm(forms.ModelForm):
    class Meta:
        model = TripPlan
        fields = ['title', 'content', 'days']
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
        }
    
    def clean_days(self):
        days = self.cleaned_data.get('days')
        if days and (days < 1 or days > 30):
            raise forms.ValidationError('游玩天数必须在1-30天之间')
        return days

