from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name','memo','sex',) #'age'
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder':'記入例：バッツ'}),
                    #'age': forms.NumberInput(attrs={'min':1}),
                    'memo': forms.Textarea(attrs={'rows': 4, 'placeholder':'記入例：水弱体化バースト'}),
                    'sex': forms.RadioSelect(),

                  }
