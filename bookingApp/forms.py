from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['visit_date', 'quantity']
        widgets = {
            'visit_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'min': str(date.today())  # 不允许选择今天之前的日期
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 10,
                'value': 1
            })
        }
        labels = {
            'visit_date': '游玩日期',
            'quantity': '票数',
        }
    
    def clean_visit_date(self):
        visit_date = self.cleaned_data.get('visit_date')
        if visit_date and visit_date < date.today():
            raise forms.ValidationError('游玩日期不能是过去的日期')
        return visit_date
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity and (quantity < 1 or quantity > 10):
            raise forms.ValidationError('票数必须在1-10之间')
        return quantity

