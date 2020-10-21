from django import forms
from .models import Post, Vehiculo


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ("title", "text")


class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo

        fields = ("placa", "referencia", "nota", "estaeliminado", "marca")
