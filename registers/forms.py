#Django
from django import forms
#Models
from .models import Registry

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(forms.ModelForm):
    '''register model form'''
    class Meta:
        model = Registry
        fields = ('plant_name','week_control', 'water_consuption','size_control', 'picture')

        widgets = {
            'week_control': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control', 'placeholder': self.snake_to_word(f)})

    @staticmethod
    def snake_to_word(word):
        """ Change snake case to word """
        return ' '.join(x.capitalize() or '_' for x in word.split('_'))