from django import forms
from .models import *
##from .models import Userdata

column, row = 2, 12
MONTH = [[0 for _ in range(column)] for _ in range(row) ]

count = 1910
column, row = 2, 113
YEAR = [[0 for _ in range(column)] for _ in range(row) ]

column, row = 2, 31
DAY = [[0 for _ in range(column)] for _ in range(row) ]


class SignupForm(forms.Form):
    
    for i in range(12):
        for j in range(2):
            MONTH[i][j] = str(i+1)

    for i in range(113):
        for j in range(2):
            YEAR[i][j] = str(count)
        count += 1
            

    for i in range(31):
        for j in range(2):
            DAY[i][j] = str(i+1)

    GENDER = [
        ['MAN', '男'],
        ['WOMAN', '女']
    ]

    username = forms.CharField(label = '姓名', max_length=10, widget=forms.TextInput(attrs={'class':'form-control', 'style':'width:100%'}))
    year = forms.ChoiceField(label = '出生年', choices = YEAR)
    month = forms.ChoiceField(label = '月', choices = MONTH)
    day = forms.ChoiceField(label = '日', choices = DAY)
    gender = forms.ChoiceField(label = '性別', choices = GENDER)
    Photos = forms.ImageField(label = '大頭貼', )

