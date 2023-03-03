from django import forms
from .models import uploadImg

class uploadForm(forms.ModelForm):
    class Meta:
        model = uploadImg
        fields = '__all__'
        labels = {'image':''}
