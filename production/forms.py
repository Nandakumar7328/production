from django import forms 

class myFile(forms.Form):
    file_name = forms.ChoiceField(widget=forms.TextInput(attrs={'class':'form-control'}))
    file_one = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    file_two = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    file_last = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))