from django import forms
from .models import Item, Bill
from django.forms.models import inlineformset_factory


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item

        exclude = ()


ItemFormSet = inlineformset_factory(
    Bill,
    Item,
    form=ItemForm,
    extra=1,
)
