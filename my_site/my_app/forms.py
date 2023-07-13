from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     name = forms.CharField(label='이름', max_length=10)
#     email = forms.EmailField(label='이메일')
#     review = forms.CharField(label='여기에 후기 작성', 
#                              widget=forms.Textarea(attrs={'class':'myform',
#                                                           'rows':'2','cols':'20'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # 모든 모델필드를 폼 필드로 사용
        
        labels = {
            'name' : '이름',
            'email' : '이메일',
            'stars' : '별점',
        }
        
        error_messages = {
            'stars' :{
                    'min_value' : '최소 1점은 주셔야 합니다.',
                    'max_value' : '최대 5점까지만 주실 수 있습니다.',
                },
        }
        
class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)