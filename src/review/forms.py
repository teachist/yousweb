from django import forms
from django.forms import ModelForm
from django.forms import inlineformset_factory
from .models import Review


class ReviewForm(forms.Form):
    # customer_name = forms.CharField(required=True, max_length=200, help_text='请输入你的客户名称', label='客户名称')
    # phone = forms.CharField(required=True, max_length=11, label='联系方式')
    # comment = forms.CharField(widget=forms.Textarea, label='更多建议')
    STARS_CHOCIES = (
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Sarts'),
        (6, 'Five Sarts'),
        (7, 'Five Sarts'),
        (8, 'Five Sarts'),
        (9, 'Five Sarts'),
    )
    # front stuff review
    ft_star = forms.ChoiceField(choices=STARS_CHOCIES, label="前台服务评分")
    # designer review
    ds_star = forms.ChoiceField(choices=STARS_CHOCIES, label="设计服务评分")
    # transfor review
    tf_star = forms.ChoiceField(choices=STARS_CHOCIES, label="配送服务评分")

    # start = forms.ChoiceField()

    # comment
