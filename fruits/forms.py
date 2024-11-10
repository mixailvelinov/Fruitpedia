from fruits.models import Fruit
from django import forms


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']

        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image': forms.TextInput(attrs={'placeholder': 'Fruit image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
        }



class DeleteFruitForm(CreateFruitForm):
    def __init__(self, *args, **kwargs):
        super(DeleteFruitForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True