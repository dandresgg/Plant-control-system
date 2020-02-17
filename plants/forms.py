#Django
from django import forms
#Models
from .models import Plants

class PlantsFormat(forms.ModelForm):
    '''plants format'''
    class Meta():
        model = Plants
        fields = ('plant_name','plant_class','plant_type','active_nutrients','noactive_nutrients')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control', 'placeholder': self.snake_to_word(f)})

    @staticmethod
    def snake_to_word(word):
        """ Change snake case to word """
        return ' '.join(x.capitalize() or '_' for x in word.split('_'))