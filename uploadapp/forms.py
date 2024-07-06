from django import forms
from uploadapp.models import *


class UploadForm(forms.ModelForm):
    
    class Meta:
        model = UploadImage
        fields = "__all__"
