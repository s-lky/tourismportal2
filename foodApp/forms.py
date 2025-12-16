from django import forms
from .models import FoodRecommendation

class FoodRecommendationForm(forms.ModelForm):
    """美食推荐表单"""
    
    class Meta:
        model = FoodRecommendation
        fields = ['food_name', 'location', 'reason']
        labels = {
            'food_name': '美食名称',
            'location': '地点',
            'reason': '推荐理由',
        }
        widgets = {
            'food_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入美食名称，如：虾饺、烧鹅、肠粉等'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '请输入具体地点，如：广州市天河区xxx餐厅'
            }),
            'reason': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': '请详细描述推荐理由，如：口味、特色、价格等...'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 添加必填字段标识
        self.fields['food_name'].required = True
        self.fields['location'].required = True
        self.fields['reason'].required = True
