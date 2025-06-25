from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, IPO

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email") 

class IPOForm(forms.ModelForm):
    class Meta:
        model = IPO
        fields = ['company', 'price_band', 'open_date', 'close_date', 'issue_size', 'issue_type', 'listing_date', 'status', 'ipo_price', 'listing_price', 'listing_gain', 'current_market_price', 'current_return']
        widgets = {
            'open_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'close_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'listing_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        # Make the specified fields not required
        for fname in ['ipo_price', 'listing_price', 'listing_gain', 'current_market_price', 'current_return']:
            self.fields[fname].required = False 

    def clean(self):
        cleaned_data = super().clean()
        for fname in ['ipo_price', 'listing_price', 'listing_gain', 'current_market_price', 'current_return']:
            if cleaned_data.get(fname) in ['', None]:
                cleaned_data[fname] = None
        return cleaned_data 