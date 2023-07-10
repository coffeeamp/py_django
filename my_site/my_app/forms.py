from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(label='이름', max_length=10)
    email = forms.EmailField(label='이메일')
    review = forms.CharField(label='여기에 후기 작성', widget=forms.Textarea)